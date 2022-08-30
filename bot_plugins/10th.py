from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

@on_command('test10th')
async def _(session: CommandSession):
    await session.send('successful!')


@on_natural_language(keywords={'test10th'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, 'test10th')
