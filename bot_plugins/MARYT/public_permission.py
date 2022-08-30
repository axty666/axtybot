from nonebot import SenderRoles
from .data_load import load_yaml

# 调用函数 写个全局变量先
result = load_yaml()

ban_people = result['Permission']['BanQQ']
allow_group = result['Permission']['AllowGroup']
ban_group = result['Permission']['BanGroup']

def public_permission(sender: SenderRoles):
    return sender.from_group(allow_group) and not sender.sent_by(ban_people) and not sender.from_group(ban_group)
