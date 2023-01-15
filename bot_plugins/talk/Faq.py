from nonebot import on_command, CommandSession, SenderRoles
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_load import load_yaml
from .public_permission import public_permission

# 调用函数 写个全局变量先

result = load_yaml()



@on_command(result['Daily']['TogetherTuan']['FirstKey'], aliases=result['Daily']['TogetherTuan']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['Daily']['TogetherTuan']['Send'])


@on_natural_language(keywords=result['Daily']['TogetherTuan']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['Daily']['TogetherTuan']['FirstKey'])


@on_command(result['Daily']['TogetheBaihua']['FirstKey'], aliases=result['Daily']['TogetheBaihua']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['Daily']['TogetheBaihua']['Send'])


@on_natural_language(keywords=result['Daily']['TogetheBaihua']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['Daily']['TogetheBaihua']['FirstKey'])


@on_command(result['Daily']['FatBaihua']['FirstKey'], aliases=result['Daily']['FatBaihua']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['Daily']['FatBaihua']['Send'])


@on_natural_language(keywords=result['Daily']['FatBaihua']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['Daily']['FatBaihua']['FirstKey'])

@on_command(result['Daily']['DogTuan']['FirstKey'], aliases=result['Daily']['DogTuan']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['Daily']['DogTuan']['Send'])

@on_natural_language(keywords=result['Daily']['DogTuan']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['Daily']['DogTuan']['FirstKey'])


@on_command(result['Daily']['Eat']['FirstKey'], aliases=result['Daily']['Eat']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    for value in result['Daily']['Eat']['Send']:
        await session.send(value)

@on_natural_language(keywords=result['Daily']['Eat']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['Daily']['Eat']['FirstKey'])


@on_command(result['Daily']['Host']['FirstKey'], aliases=result['Daily']['Host']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['Daily']['Host']['Send'])


@on_natural_language(keywords=result['Daily']['Host']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['Daily']['Host']['FirstKey'])


@on_command(result['Daily']['Sex']['FirstKey'], aliases=result['Daily']['Sex']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    for value in result['Daily']['Sex']['Send']:
        await session.send(value)


@on_natural_language(keywords=result['Daily']['Sex']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['Daily']['Sex']['FirstKey'])


@on_command(result['Daily']['SpringFestivalGala']['FirstKey'], aliases=result['Daily']['SpringFestivalGala']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['Daily']['SpringFestivalGala']['Send'])


@on_natural_language(keywords=result['Daily']['SpringFestivalGala']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['Daily']['SpringFestivalGala']['FirstKey'])

def AXDontKnown(sender: SenderRoles):
    return sender.sent_by(result['DailyPermission']['AXdontknown']['Permission']['QQ'])

@on_command(result['DailyPermission']['AXdontknown']['FirstKey'], aliases=result['DailyPermission']['AXdontknown']['Aliases'], permission=AXDontKnown, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['DailyPermission']['AXdontknown']['Send'])

@on_natural_language(keywords=result['DailyPermission']['AXdontknown']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['DailyPermission']['AXdontknown']['FirstKey'])
