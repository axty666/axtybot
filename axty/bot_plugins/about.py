from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


__plugin_name__ = '关于axtybot'
__plugin_usage__ = (
    '有关的axtybot的信息和感谢列表'
)

@on_command('aboutaxtybot', aliases={'关于axtybot', '/ababout', '/ab关于'})
async def _(session: CommandSession):
    await session.send('''A MARYT PLAYER BOT NAMED axtybot
version:1.9.20220403_MARYT10th
版本：1.9.20220403_MARYT10th
(将升级到2.x版本，敬请期待)
如果你想与axty一起整点活可以私聊axty，若了解Python编程可以前往https://github.com/axty666/axtybot 一起整活并fork you!
---------
(axty大爱Fantasy_Z(逃)''')

@on_natural_language(keywords={'/ababout', '/ab关于'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'aboutaxtybot')