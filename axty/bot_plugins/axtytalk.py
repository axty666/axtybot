from nonebot import session, on_notice, NoticeSession
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg

@on_command('咋抱团取暖', aliases={'有无一块玩的', '有无一起玩的'})
async def _(session: CommandSession):
    await session.send('佬可以输入./cz加入一个城镇')
    await session.send('或者在./cz里面创建一个城镇(需要1000游戏币)(')

@on_natural_language(keywords={'一块玩', '一起玩', '抱团'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '咋抱团取暖')

@on_command('咋去暮色', aliases={'怎样去暮色'})
async def _(session: CommandSession):
    await session.send('佬请使用"沾满魔力的铜钥匙"代替钻石来开启暮色门')
    await session.send('铜钥匙可以在jei里面查找到（')

@on_natural_language(keywords={'去暮色'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '咋去暮色')

@on_command('咋创建玩家组织', aliases={'怎样创建玩家组织'})
async def _(session: CommandSession):
    await session.send('佬可以找管理组进行一个的询问（')
    await session.send('ps:佬如果想整点官网的话可以私聊axty(')

@on_natural_language(keywords={'创建玩家组织'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '咋创建玩家组织')

@on_command('咋给钱', aliases={'怎样打钱'})
async def _(session: CommandSession):
    await session.send('./pay 玩家id 钱数')
    await session.send('示例：/pay axty 0.01')

@on_natural_language(keywords={'咋打钱', '咋给钱', '怎样给钱'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '咋给钱')

@on_command('去商店', aliases={'商店在哪'})
async def _(session: CommandSession):
    await session.send('./sg 高价收购 ./sd 特价商店')
    await session.send('以上两个的物品定时刷新(价格优惠)')
    await session.send('如果上面两个都没有的话可以./spawn回到主城，然后沿着左前方的路走')

@on_natural_language(keywords={'去商店', '商店在哪', '主城商店', '商店'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '去商店')
    
@on_command('共享啊团', aliases={'扫码啊团', '共享阿团', '扫码阿团'})
async def _(session: CommandSession):
    await session.send('扫码就骑!')

@on_natural_language(keywords={'共享啊团', '扫码啊团', '共享阿团', '扫码阿团'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '共享啊团')

@on_command('挣钱', aliases={'得钱'})
async def _(session: CommandSession):
    await session.send('目前服务器内有两种钱,平常交易时的游戏币')
    await session.send('游戏币可以通过每日签到，去商店那边卖东西来获得(')
    await session.send('另一种就是城镇币，佬可以在./cz那边创建一个城镇或者加入一个城镇后以捐城镇币的方式获得')
    await session.send('城镇币可以用来升级城镇有关的东西')

@on_natural_language(keywords={'挣钱', '得钱', '钱怎么弄'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '挣钱')

@on_command('升级城镇', aliases={'城镇升级'})
async def _(session: CommandSession):
    await session.send('佬可以用城镇币来升级城镇有关的东西（')
    await session.send('佬在./cz那边创建一个城镇或者加入一个城镇后以捐城镇币的方式得城镇币（')

@on_natural_language(keywords={'升级城镇', '城镇升级', '给城镇'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '升级城镇')

@on_command('开箱子', aliases={'打开箱子'})
async def _(session: CommandSession):
    await session.send('箱子锁')

@on_natural_language(keywords={'开箱子', '开箱子', '解锁箱子', '开我的箱子'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '开箱子')

#@on_command('不懂就问', permission=lambda sender_id: 3116886930 | Container[2153069097])
@on_command('不懂就问', permission=lambda sender: sender.is_superuser)
async def _(session: CommandSession):
    await session.send('块爬块爬@axty')

@on_natural_language(keywords={'不懂就问', '哪个孙子', '那个孙子', '天天骚扰我'}, only_to_me=False, permission=lambda sender: sender.is_superuser)
async def _(session: NLPSession):
    return IntentCommand(90.0, '不懂就问')

@on_command('主机名', aliases={'主鸡名'})
async def _(session: CommandSession):
    await session.send('ping 域名/ip中的域名/ip')

@on_natural_language(keywords={'主机名是什么', '主鸡名是什么', '主机名是啥', '主机名到底是什么'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '主机名')

@on_command('菜单', aliases={'蔡丹'})
async def _(session: CommandSession):
    await session.send('指令')
    await session.send('目前(10th)服务器内无菜单')

@on_natural_language(keywords={'有无菜单', '菜单的指令', '有没有菜单', '菜单的命令', '有菜单'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '菜单')

@on_command('地皮', aliases={'地皮世界'})
async def _(session: CommandSession):
    await session.send('服务器内无地皮')
    await session.send('佬如果有这方面的需要可以考虑领地（')

@on_natural_language(keywords={'有无地皮', '地皮的指令', '有没有地皮', '地皮的命令', '有地皮'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '地皮')

@on_command('随机传送', aliases={'随机传送'})
async def _(session: CommandSession):
    await session.send('服务器内无随机传送')
    await session.send('还请佬能够理解')

@on_natural_language(keywords={'有无随机传送', '随机传送的指令', '有没有随机传送', '随机传送的命令', '有随机传送'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '随机传送')

@on_command('连锁', aliases={'连锁'})
async def _(session: CommandSession):
    await session.send('服务器内无连锁挖矿')
    await session.send('还请佬能够理解')
    await session.send('但是有一键砍树，按shift可取消连锁砍树')  
    await session.send('一键砍树所需要的时间与砍的原木的数量成正比（')

@on_natural_language(keywords={'有无连锁', '连锁的指令', '有没有连锁', '连锁的命令', '有连锁'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '连锁')

@on_command('来点涩图', aliases={'请求色色'})
async def _(session: CommandSession):
    await session.send('好的，给！')
    await session.send('https://www.aliyundrive.com/s/GKGaBRsAtRL')

@on_natural_language(keywords={'涩图', '色图', '瑟图', '色色', '瑟瑟', '涩涩'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '来点涩图')

@on_command('春晚合集', aliases={'春晚大合集'})
async def _(session: CommandSession):
    await session.send('''「春晚1956-2021【4K】」，链接:https://www.aliyundrive.com/s/GKGaBRsAtRL
''')

@on_natural_language(keywords={'春晚合集', '春晚大全', '以前的春晚', '有无春晚', '重温春晚'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '春晚合集')

#@on_command('fz不在家', permission=lambda sender_id: 3116886930 | Container[2153069097])
@on_command('fz不在家', permission=lambda sender: sender.is_superuser)
async def _(session: CommandSession):
    await session.send('@Fantasy_Z')

@on_natural_language(keywords={'fz不在家', '老公不在家'}, only_to_me=False, permission=lambda sender: sender.is_superuser)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'fz不在家')

Fantasy_permission = lambda sender: sender.sent_by(self, 2123775697 | Container[2118630546])
@on_command('ax不在家', permission=Fantasy_permission)
async def _(session: CommandSession):
    await session.send('@Fantasy_Z')

Fantasy_permission = lambda sender: sender.sent_by(self, 2123775697 | Container[2118630546])
@on_natural_language(keywords={'老婆不在家', 'ax不在家'}, only_to_me=False, permission=Fantasy_permission)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'ax不在家')