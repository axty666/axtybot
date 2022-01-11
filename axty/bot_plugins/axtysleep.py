from typing import List
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import randint

List = [
    "'你周围有怪物游荡'"
    ,"你被刻意的游戏设计炸死了"
    ,"你只能在夜晚或雷暴天睡觉"
    ,"床离你太远了"
    ]
async def axtysleep():
    Thing = List[randint(0,len(List)-1)]
    return Thing

@on_command('睡觉', aliases={'入眠'})
async def _(session: CommandSession):
    AXSL = await axtysleep()
    await session.send(AXSL)

@on_natural_language(keywords={'睡觉', '入眠'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '睡觉')
