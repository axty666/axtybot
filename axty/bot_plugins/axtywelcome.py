from nonebot import session, on_notice, NoticeSession
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
allowGroups = [640614812]
@on_notice('group_increase')
async def _(session: NoticeSession):
    group_id = session.event.group_id
    if group_id in allowGroups:
        welcomeMessage = '[CQ:at,qq='+str(session.event.user_id)+']'+'迎新佬！'
        welcomeMessage2 = '佬记得看客户端的txt文件'
        welcomeMessage3 = '群文件里面有客户端'
        await session.send(welcomeMessage)
        await session.send(welcomeMessage2)
        await session.send(welcomeMessage3)

@on_command('迎新佬')
async def _(session: CommandSession):
    await session.send('佬记得看客户端的txt文件')
    await session.send('群文件里面有客户端')

@on_natural_language(keywords={'迎新佬', '喜迎'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '迎新佬')

@on_command('佬记得看客户端的txt文件')
async def _(session: CommandSession):
    await session.send('群文件里面有客户端')

@on_natural_language(keywords={'佬记得看客户端的txt文件', '佬记得看'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '佬记得看客户端的txt文件')