from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_load import load_yaml
from .public_permission import public_permission
result = load_yaml()

@on_command(result['Faq']['Auto']['FirstKey'], aliases=result['Faq']['Auto']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['Faq']['Auto']['Send'])


@on_natural_language(keywords=result['Faq']['Auto']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['Faq']['Auto']['FirstKey'])
