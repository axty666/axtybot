from nonebot import on_notice, NoticeSession, MessageSegment
from .data_load import load_yaml

# 调用函数 写个全局变量先
result = load_yaml()
Group = [result['Welcome']['Groups']]

@on_notice('group_increase')
async def _(session: NoticeSession):
    group_id = session.event.group_id
    if group_id in Group:
        message = MessageSegment.at(session.event.user_id) + result['Welcome']['Send'][0]
        message2 = result['Welcome']['Send'][1]
        message3 = result['Welcome']['Send'][2]
        message4 = result['Welcome']['Send'][3]
        await session.send(message)
        await session.send(message2)
        await session.send(message3)
        await session.send(message4)
