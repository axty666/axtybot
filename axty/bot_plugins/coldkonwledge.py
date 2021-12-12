from typing import List
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import randint

__plugin_name__ = '冷知识'
__plugin_usage__ = '''
输入冷知识随机抽一手佬们的冷知识
'''
List = [
    "g-c-z.cc的二级域名可以找axty搞个"
    ,"老乌龟其实不是王八"
    ,"test"
    ,"axty也喜欢依神紫苑(所以拔刀⑧各位)(逃"
    ,"广场镇官网底下有个↓劲↑爆↓歌↑单"
    ,"axty曾经有许多花活设想(但整出来就是怪活了)"
    ,"axty现在濒临破产，如有乐于捐助的可以私聊"
    ,"我是大陸北方的一個網友，我對於你剛剛的話特別感興趣，請加我tg於我仔細探討"
    ,"如果当前气温低于15°，那人就会感觉到冷"
    ,"如果你感觉到冷，那说明你的周围很冷"
    ,"共享啊团，扫码就骑！"
    ,"寄！"
    ,"该青年大学习了团团们（"
    ,"三分钟前热心的阿苟为你检察了下牛牛的健康，请放心，你的牛牛非常健康"
    ,"念哼哼哈哈有时候会不小心喊成哼↑哼↓啊啊啊"
    ,"今天风和日丽,晴空万里,而你，就该绝版。"
    ,"axty天天说跑路但仍然没跑路(因为懒()"
    ,"不能理解对方的时候可以试着ping下对方的IP地址"
    ,"从前有只可爱的狗狗叫牧牧，后来他死于一场意外，他的主人为了纪念他养了第二条可爱的狗狗叫怀念牧牧"
    ,"据说ax有只可爱的狗狗叫怀念怀念牧牧"
    ,"赞美Fantasy_Z"
    ,"我，秦始皇，打钱!"
    ,"白桦的前任女儿:被ax用心调教(并没有)过后的小树妖(盖亚萌典3mod的小树妖)"
    ,"axty喜欢Fantasy_Z"
    ]
async def coldknowledge():
    Thing = List[randint(0,len(List)-1)]
    return "冷知识："+Thing

@on_command('冷知识',aliases=('冷知识'))
async def _(session: CommandSession):
    CKL = await coldknowledge()
    await session.send(CKL)

@on_natural_language(keywords={'冷知识'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '冷知识')
