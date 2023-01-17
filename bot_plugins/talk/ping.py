from nonebot import on_command, CommandSession
import subprocess
from jieba import posseg
from .data_load import load_yaml

# 调用函数 写个全局变量先
load_data = result = load_yaml()

__plugin_name__ = result['Ping']['Name']
__plugin_usage__ = result['Ping']['Usage']


@on_command(result['Ping']['FirstKey'], aliases=result['Ping']['Aliases'], only_to_me=False)
async def _(session: CommandSession):
# 取得消息的内容，并且去掉首尾的空白符
    host_port = session.current_arg_text.strip()
    if not host_port:
        host_port = (await session.aget(prompt=result['Ping']['Not_host'])).strip()
        while not host_port:
            host_port = (await session.aget(prompt=result['Ping']['While_not_host'])).strip()
        else:
            await session.send(result['Ping']['Get_host'])
    ping_result = await get_ping_of_result(host_port)
    await session.send(ping_result)

async def get_ping_of_result(host_port: str) -> str:
    try:
        host = host_port.split(":", 1)[0]
        port = host_port.split(":", 1)[1]
    except:
        host = host_port.split(" ", 1)[0]
        port = host_port.split(" ", 1)[1]

    try:
        tcping_result = subprocess.Popen(
            args=['tcping', host, '-c', '4', '-p', port], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        return f'{host}' + load_data['Ping']['Successful'] + f'{tcping_result.stdout.read()}' or f'{tcping_result.stderr.read()}'
    except:
        return f'{host}' + load_data['Ping']['Failed']
