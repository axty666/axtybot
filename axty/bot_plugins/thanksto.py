from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


__plugin_name__ = 'axtybot感谢名单'
__plugin_usage__ = (
    '有关的axtybot的信息和感谢列表'
)

@on_command('axtybotthanksto', aliases={'axtybot感谢名单', '/abthanks', '/ab感谢名单'})
async def _(session: CommandSession):
    await session.send('''感谢maryt/vanilo管理组对于本项目的支持
感谢苟佬(azurePh03nix)解决了咱提出的一些写bot时碰见的低级问题
感谢Fantasy_Z对于本项目持续提供的好创意
感谢波凌佬的捉虫(反馈错别字)
感谢maryt/vanilo玩家对于咱这个bot的欢迎
本bot参考了开源项目Box-s-ville/luciabot，在此向项目开发者致谢！
本bot参考了开源项目nonebot/nonebot的教程,在此向项目开发者致谢！
本bot参考了MARYTbot的代码，在此向苟佬致谢！
---------
(axty大爱Fantasy_Z(逃)''')

@on_natural_language(keywords={'/abthanks', '/ab感谢名单'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'axtybotthanksto')