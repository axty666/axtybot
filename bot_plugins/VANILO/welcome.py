from email.headerregistry import Group
from nonebot import on_notice, NoticeSession
from .data_load import load_yaml

# 调用函数 写个全局变量先
result = load_yaml()
Group = [result['Welcome']['Group']]

@on_notice('group_increase')
async def _(session: NoticeSession):
    group_id = session.event.group_id
    if group_id in Group:
        for value in result['Welcome']['Send']:
            await session.send(value)
