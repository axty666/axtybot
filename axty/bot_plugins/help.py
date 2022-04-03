from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


__plugin_name__ = '帮助'
__plugin_usage__ = (
    '介绍关键词'
)

@on_command('/abhelp', aliases={'/ab帮助', '/help', '/帮助'})
async def _(session: CommandSession):
    await session.send('''本bot支持以下关键词：
一起玩m服、怎样去暮色、怎样创建玩家组织、咋给别人钱、咋去商店、怎么挣钱、怎样给城镇升级、咋打开箱子、添加好友、有无菜单、怎么去地皮世界、怎么安装光影、怎么安装材质包、给别人领地权限、怎么随机传送、有无连锁挖矿、签到里面有啥、游戏币有啥用、咋查看我的账户余额、咋看我多么富
MARYTBOT支持的关键词：
简介、模组列表、怎么注册、怎么安装客户端、安装Java、苟佬的完美教室、领地插件介绍、箱子锁的权限列表、服务器内常用命令、崩溃了咋办、服务器玩法、怎么赞助M服、老黄历
整活关键词：
共享啊团、联动啊团、联动白桦和狗蛋、胖胖白桦、狗比狗团、吃什么、主机名是什么、请求涩涩、春晚合集
(如果内容过多会实装/ab欲知更多)
(axty大爱Fantasy_Z(逃)''')

@on_natural_language(keywords={'/ab帮助', '/abhelp'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '/abhelp')