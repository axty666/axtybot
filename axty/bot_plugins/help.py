from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


__plugin_name__ = '帮助'
__plugin_usage__ = (
    '介绍每个支持的功能'
    '讲句“帮助”康康咱支持啥功能（'
    '“帮助 支持的功能的名字” 获取对应详细介绍'
)

@on_command('axtyhelp', aliases={'axty帮助'})
async def _(session: CommandSession):
    await session.send('''事axty边学边写滴bot!,希望整的活能给佬来点帮助（
---------
以下是axty整的正常活
---------
帮助--显示本条信息
关于axtybot--显示感谢信息和有关信息
---------
以下是axty整的怪活
---------
冷知识--输入“冷知识”随机抽取一条冷知识
随机天气--输入“随机天气”然后输入任意内容来感受axty的怪活
共享啊团--扫码就骑!
联动啊团--新春八折!
---------
如果恁想与axty一起整点活可以私聊axty，若恁也了解Python编程和github也可以可以前往
https://github.com/axty666/axtybot 一起整活并fork you!
关于有的消息无法识别请参见https://github.com/nonebot/nonebot/issues/286
(axty大爱Fantasy_Z(逃)''')