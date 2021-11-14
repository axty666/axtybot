from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


__plugin_name__ = '帮助'
__plugin_usage__ = (
    '介绍每个支持的功能'
    '讲句“帮助”康康咱支持啥功能（'
    '“帮助 支持的功能的名字” 获取对应详细介绍'
)

@on_command('axtyhelp', aliases={'axty帮助', '关于axtybot'})
async def _(session: CommandSession):
    await session.send('''事axty边学边写滴bot!,希望整的这点活能给佬来点帮助（
---------以下是axty整的正常活
帮助--------显示本条信息
---------以下是axty整的怪活
冷知识------输入“冷知识”随机抽取一条冷知识
天气--------输入“天气”然后输入任意内容来感受axty的怪活
---------以下是本bot滴感谢信息
感谢maryt/vanilo管理组对于咱这个bot滴支持
感谢苟佬(azurePh03nix)解决了咱提出的一些写bot时碰见的低级问题
感谢maryt/vanilo玩家对于咱这个bot的欢迎
本bot参考了开源项目Box-s-ville/luciabot，在此向项目开发者致谢！
本bot参考了开源项目nonebot/nonebot的教程,在此向项目开发者致谢！
本bot参考了MARYTbot的代码，在此向苟佬致谢！
如果恁想与axty一起整点活可以私聊axty
如果恁想与axty一起整点活且了解Python编程可以前往https://github.com/axty666/axtybot 一起整活并fork you!
(axty大爱Fantasy_z(逃)
''')