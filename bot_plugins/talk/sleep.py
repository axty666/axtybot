from typing import List
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import randint
from .data_load import load_yaml
from .public_permission import public_permission

# 调用函数 写个全局变量先
result = load_yaml()

# 插件的介绍
__plugin_name__ = result['Sleep']['Name']
__plugin_usage__ = result['Sleep']['Usage']

List = result['Sleep']['List']
async def axtysleep():
    Thing = List[randint(0,len(List)-1)]
    return Thing


@on_command(result['Sleep']['FirstKey'], aliases=result['Sleep']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    AXSL = await axtysleep()
    await session.send(AXSL)


@on_natural_language(keywords=result['Sleep']['Keywords'], permission=public_permission, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, result['Sleep']['FirstKey'])
