from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg

@on_command('咋抱团取暖', aliases={'有无一块玩的', '有无一起玩的'})
async def _(session: CommandSession):
    await session.send('佬可以输入./cz加入一个城镇')
    await session.send('或者在./cz里面创建一个城镇(需要1000游戏币)(')

@on_natural_language(keywords={'一块玩', '一起玩', '抱团'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '咋抱团取暖')

@on_command('咋去暮色', aliases={'怎样去暮色'})
async def _(session: CommandSession):
    await session.send('佬请使用"沾满魔力的铜钥匙"代替钻石来开启暮色门')
    await session.send('铜钥匙可以在jei里面查找到（')

@on_natural_language(keywords={'去暮色'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '咋去暮色')

@on_command('咋创建玩家组织', aliases={'怎样创建玩家组织'})
async def _(session: CommandSession):
    await session.send('佬可以找管理组进行一个的询问（')
    await session.send('ps:佬如果想整点官网的话可以私聊axty(')

@on_natural_language(keywords={'创建玩家组织'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '咋创建玩家组织')

@on_command('咋给钱', aliases={'怎样打钱'})
async def _(session: CommandSession):
    await session.send('./pay 玩家id 钱数')
    await session.send('示例：/pay axty 0.01')

@on_natural_language(keywords={'咋打钱', '咋给钱', '怎样给钱'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '咋给钱')

@on_command('去商店', aliases={'商店在哪'})
async def _(session: CommandSession):
    await session.send('./sg 高价收购 ./sd 特价商店')
    await session.send('以上两个的物品定时刷新(价格优惠)')
    await session.send('如果上面两个都没有的话可以./spawn回到主城，然后沿着左前方的路走')

@on_natural_language(keywords={'去商店', '商店在哪', '主城商店', '商店'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '去商店')
    
@on_command('共享啊团', aliases={'扫码啊团', '共享阿团', '扫码阿团'})
async def _(session: CommandSession):
    await session.send('扫码就骑!')

@on_natural_language(keywords={'共享啊团', '扫码啊团', '共享阿团', '扫码阿团'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '共享啊团')

@on_command('挣钱', aliases={'得钱'})
async def _(session: CommandSession):
    await session.send('目前服务器内有两种钱,平常交易时的游戏币')
    await session.send('游戏币可以通过每日签到，去商店那边卖东西来获得(')
    await session.send('另一种就是城镇币，佬可以在./cz那边创建一个城镇或者加入一个城镇后以捐城镇币的方式获得')
    await session.send('城镇币可以用来升级城镇有关的东西')

@on_natural_language(keywords={'挣钱', '得钱', '钱怎么弄'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '挣钱')

@on_command('升级城镇', aliases={'城镇升级'})
async def _(session: CommandSession):
    await session.send('佬可以用城镇币来升级城镇有关的东西（')
    await session.send('佬在./cz那边创建一个城镇或者加入一个城镇后以捐城镇币的方式得城镇币（')

@on_natural_language(keywords={'升级城镇', '城镇升级', '给城镇'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '升级城镇')