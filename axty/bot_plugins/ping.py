from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from pythonping import ping


__plugin_name__ = 'ping'
__plugin_usage__ = '查看指定主机名与axtybotの连接情况'


@on_command('ping')
async def ping(session: CommandSession):
    host = session.get('host', prompt='主机名？')
    start_ping_result = await get_ping_of_result(host)
    await session.send(start_ping_result)

@ping.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['host'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('整点主机名⑧')

    session.state[session.current_key] = stripped_arg

async def get_ping_of_result(host: str) -> str:
    ping_result = await ping_results(host)
    return f'{host}与axtybot的连接情况'+ str(ping_result)

async def ping_results(host):
    ping ('{host}')