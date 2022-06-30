from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from pythonping import ping
from jieba import posseg
import tldextract


__plugin_name__ = 'ping'
__plugin_usage__ = '查看指定主机名与axtybotの连接情况'


@on_command('ping', aliases=('PING', 'Ping'))
async def _(session: CommandSession):
# 取得消息的内容，并且去掉首尾的空白符
    host = session.current_arg_text.strip()
    if not host:
        host = (await session.aget(prompt='主机名是什么捏？')).strip()
        while not host:
            host = (await session.aget(prompt='主机名不能为空的捏')).strip()
        else:
            await session.send('好耶，咱正在尝试ping一波')
    ping_result = await get_ping_of_result(host)
    await session.send(ping_result)

async def get_ping_of_result(host: str) -> str:
    try:
            result = ping (host)
            return f'{host}与axtybot的连接情况：\n'+ str(result)
    except:
            return f'{host}与axtybot连接出错，请自行排查'

@on_natural_language(keywords={'ping', 'PING'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'ping')