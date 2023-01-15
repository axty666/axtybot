from typing import List
from nonebot import on_command, CommandSession, MessageSegment
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import randint
from .data_load import load_yaml
from .public_permission import public_permission

# 调用函数 写个全局变量先
result = load_yaml()

# 插件的介绍
__plugin_name__ = result['ShareTuan']['Name']
__plugin_usage__ = result['ShareTuan']['Usage']

List = result['ShareTuan']['List']

@on_command(result['ShareTuan']['FirstKey'],
            aliases=result['ShareTuan']['Aliases'],
            permission=public_permission,
            only_to_me=False)
async def _(session: CommandSession):
    Thing = List[randint(0, len(List)-1)]
    if randint(0, len(List)-1) == 6:
        Thing = List[6] + MessageSegment.image(result['ShareTuan']['Listpic'])
    await session.send(Thing)


@on_natural_language(keywords=result['ShareTuan']['Keywords'],
                    permission=public_permission,
                    only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, result['ShareTuan']['FirstKey'])
