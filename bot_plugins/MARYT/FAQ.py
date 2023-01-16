from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot import SenderRoles

from .data_load import load_yaml
from .public_permission import public_permission

# 调用函数 写个全局变量先
result = load_yaml()

@on_command(result['FAQ']['InstallShaderPack']['FirstKey'], aliases=result['FAQ']['InstallShaderPack']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    for value in result['FAQ']['InstallShaderPack']['Send']:
        await session.send(value)

@on_natural_language(keywords=result['FAQ']['InstallShaderPack']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['FAQ']['InstallShaderPack']['FirstKey'])


@on_command(result['FAQ']['InstallResourcePack']['FirstKey'], aliases=result['FAQ']['InstallResourcePack']['Aliases'], permission=public_permission, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['FAQ']['InstallResourcePack']['Send'])


@on_natural_language(keywords=result['FAQ']['InstallResourcePack']['Keywords'], only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['FAQ']['InstallResourcePack']['FirstKey'])


def FZInGroup(sender: SenderRoles):
    return sender.sent_by(result['FAQPermission']['FZInGroup']['Permission']['QQ'])


@on_command(result['FAQPermission']['FZInGroup']['FirstKey'], permission=FZInGroup, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['FAQPermission']['FZInGroup']['Send'])


@on_natural_language(keywords=result['FAQPermission']['FZInGroup']['Keywords'], permission=FZInGroup, only_to_me=False, only_short_message=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['FAQPermission']['FZInGroup']['FirstKey'])


def AXInGroup(sender: SenderRoles):
    return sender.sent_by(result['FAQPermission']['AXInGroup']['Permission']['QQ'])


@on_command(result['FAQPermission']['AXInGroup']['FirstKey'], permission=AXInGroup, only_to_me=False)
async def _(session: CommandSession):
    await session.send(result['FAQPermission']['AXInGroup']['Send'])


@on_natural_language(keywords=result['FAQPermission']['AXInGroup']['Keywords'], permission=AXInGroup, only_to_me=False, only_short_message=False)
async def _(session: NLPSession):
    return IntentCommand(90, result['FAQPermission']['AXInGroup']['FirstKey'])
