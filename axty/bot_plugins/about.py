from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


__plugin_name__ = '关于axtybot'
__plugin_usage__ = (
    '有关的axtybot的信息和感谢列表'
)

@on_command('aboutaxtybot', aliases={'关于axtybot'})
async def _(session: CommandSession):
    await session.send('''感谢maryt/vanilo管理组对于咱这个bot滴支持
感谢苟佬(azurePh03nix)解决了咱提出的一些写bot时碰见的低级问题
感谢maryt/vanilo玩家对于咱这个bot的欢迎
本bot参考了开源项目Box-s-ville/luciabot，在此向项目开发者致谢！
本bot参考了开源项目nonebot/nonebot的教程,在此向项目开发者致谢！
本bot参考了MARYTbot的代码，在此向苟佬致谢！
如果恁想与axty一起整点活可以私聊axty，若了解Python编程可以前往https://github.com/axty666/axtybot 一起整活并fork you!
---------
(axty大爱Fantasy_z(逃)''')