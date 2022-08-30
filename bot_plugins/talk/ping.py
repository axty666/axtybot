from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from pythonping import ping
from jieba import posseg
from .data_load import load_yaml

# 调用函数 写个全局变量先
load_data = result = load_yaml()

__plugin_name__ = result['Ping']['Name']
__plugin_usage__ = result['Ping']['Usage']


@on_command(result['Ping']['FirstKey'], aliases=result['Ping']['Aliases'], only_to_me=False)
async def _(session: CommandSession):
# 取得消息的内容，并且去掉首尾的空白符
    host = session.current_arg_text.strip()
    if not host:
        host = (await session.aget(prompt=result['Ping']['Not_host'])).strip()
        while not host:
            host = (await session.aget(prompt=result['Ping']['While_not_host'])).strip()
        else:
            await session.send(result['Ping']['Get_host'])
    ping_result = await get_ping_of_result(host)
    await session.send(ping_result)

async def get_ping_of_result(host: str) -> str:
    try:
            result = ping (host)
            return f'{host}' + load_data['Ping']['Successful'] + str(result)
    except:
        return f'{host}' + load_data['Ping']['Failed']


@on_natural_language(keywords=load_data['Ping']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, load_data['Ping']['FirstKey'])
