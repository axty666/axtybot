from typing import List
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import randint
from .data_load import load_yaml
from .public_permission import public_permission

# 调用函数 写个全局变量先
result = load_yaml()
# 插件的介绍
__plugin_name__ = result['GouSay']['Name']
__plugin_usage__ = result['GouSay']['Usage']

List = result['GouSay']['List']
async def gousay():
    Thing = List[randint(0, len(List)-1)]
    return "苟说："+Thing


@on_command(result['GouSay']['FirstKey'],
            aliases=result['GouSay']['Aliases'],
            permission=public_permission,
            only_to_me=False)
async def _(session: CommandSession):
    CKL = await gousay()
    await session.send(CKL)


@on_natural_language(keywords={result['GouSay']['FirstKey']},
                        permission=public_permission,
                        only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, result['GouSay']['FirstKey'])
