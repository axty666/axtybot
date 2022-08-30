from nonebot import on_command, CommandSession
from .data_load import load_yaml
from .public_permission import public_permission

# 调用函数 写个全局变量先
result = load_yaml()

# 插件的介绍
__plugin_name__ = result['About']['Name']
__plugin_usage__ = result['About']['Usage']


# 关于插件
@on_command(result['About']['FirstKey'], aliases=result['About']['Key'], permission=public_permission)
async def abot(session: CommandSession):
    await session.send(result['About']['Send'])
