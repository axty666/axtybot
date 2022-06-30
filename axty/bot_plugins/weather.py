from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg
from aiocache import cached
from httpx import AsyncClient, HTTPError
import jieba


# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」


@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    args = session.current_arg_text.strip().split(' ', 1)
    if not args[0]:
        city = await session.aget(key='city', prompt='请问是什么城市呢？', at_sender=True)
    else:
        city = args[0]
    is_detailed = (len(args) == 2 and args[1] == '详细') or session.state.get('is_detailed')
    # 获取城市的天气预报
    try:
        func = get_current_weather_desc if is_detailed else get_weather_of_city
    except HTTPError as e:
        return f'API 服务目前不可用'
        # 向用户发送天气预报
    result = await func(city)
    await session.send(result)

async def jieba_ns(city: str) -> str:
        args = str(city)
        words = posseg.lcut(args)
        args = {}
        for word, flag in words:
            if flag == 'ns':
                city = word
                return city
            else: # 没用 鬼知道为啥删了就无法限制
                return f'请输入有效的地名！'

@cached(ttl=60)
async def get_weather_of_city(city: str) -> str:
    city = await jieba_ns(city)
    return (await fetch_text(f'https://wttr.in/{city}?format=1&lang=zh')).strip()

@cached(ttl=60)
async def get_current_weather_desc(city: str) -> str:
    _format = (
        '%l:\n'
        '+%c+%C:+%t\n'
        '+💦+Humidity:+%h\n'
        '+💧+Precipitation:+%p\n'
        '+🍃+Wind:+%w'
    )
    city = await jieba_ns(city)
    return await fetch_text(f'https://wttr.in/{city}?format={_format}&lang=zh')

async def fetch_text(uri: str) -> str:
    async with AsyncClient(headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}) as client:
        try:
            res = await client.get(uri)
            res.raise_for_status()
        except HTTPError as e:
            return f'API 服务目前不可用，或者可能输入了无效的地名'
        return res.text



@on_natural_language(keywords={'天气', '天气预报', '查天气', 'weather'}, only_to_me=False)
async def _(session: NLPSession):
    # 使用 jieba 将消息句子分词
    words = posseg.lcut(session.msg_text.strip())
    args = {}
    for word, flag in words:
        if flag == 'ns':  # ns 表示该词为地名
            args['city'] = word
            return args
        elif word in ('详细', '报告', '详情'):
            args['is_detailed'] = True
            return args

    # 置信度为 90，意为将此会话当作 'weather' 命令处理
    return IntentCommand(90, 'weather', args=args)
