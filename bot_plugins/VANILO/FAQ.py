from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot import SenderRoles

from .data_load import load_yaml
from .public_permission import public_permission

# 调用函数 写个全局变量先
result = load_yaml()


@on_command(result['FAQ']['PlayerSpawn']['FirstKey'], aliases=result['FAQ']['PlayerSpawn']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
        await session.send(result['FAQ']['PlayerSpawn']['Send'])

@on_natural_language(keywords=result['FAQ']['PlayerSpawn']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['FAQ']['PlayerSpawn']['FirstKey'])