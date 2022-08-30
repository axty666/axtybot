from nonebot import SenderRoles, on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg
from httpx import AsyncClient, HTTPError
import jieba
from random import randint
from .data_load import load_yaml

# 调用函数 写个全局变量先
load_data = result = load_yaml()

# 整点插件说明
__plugin_name__ = result['Weather']['Name']
__plugin_usage__ = result['Weather']['Usage']

# 声明权限函数 好哈人的
#def qweather(sender: SenderRoles):
#    return sender.from_group(691790710)

#随机天气的列表
List = result['Weather']['List']
async def weatherthings():
    #随机抽取一条天气
    rollweather = List[randint(0, len(List)-1)]
    return rollweather

# 注册天气命令
@on_command(result['Weather']['FirstKey'], aliases=result['Weather']['Aliases'], only_to_me=False)
async def weather(session: CommandSession):
    city = session.current_arg_text.strip()
    if not city:
        city = (await session.aget(prompt=result['Weather']['Not_args'])).strip()
        while not city:
            city = (await session.aget(prompt=result['Weather']['While_not_city'])).strip()
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)

async def jieba_ns(city: str) -> str:
    jieba.load_userdict('public/dict/full.txt')
    args = str(city)
    words = posseg.lcut(args)
    args = {}
    for word, flag in words:
        if flag == 'ns':
            city = word
            return city
        else:  # 没用 鬼知道为啥删了就无法限制
            return f'请输入有效的地名！'

async def get_weather_of_city(city: str) -> str:
    if city == result['Weather']['RollWeatherCity']:
        rollweather = await weatherthings()
        return str(rollweather)
    await jieba_ns(city)
    return (await fetch_text(f'https://wttr.in/{city}?format=1&lang=zh')).strip()

async def fetch_text(uri: str) -> str:
    async with AsyncClient(headers={'User-Agent': result['Weather']['User-Agent']}) as client:
        try:
            res = await client.get(uri)
            res.raise_for_status()
            return res.text
        except HTTPError as e:
            # raise ServiceException('API 服务目前不可用，或者可能输入了无效的地名')
            return result['Weather']['Error']
        except:
            return result['Weather']['Error']


@on_natural_language(keywords=result['Weather']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    # 置信度为 90，意为将此会话当作 'weather' 命令处理
    return IntentCommand(90, result['Weather']['FirstKey'])
