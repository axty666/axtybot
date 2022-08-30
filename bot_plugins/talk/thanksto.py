from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_load import load_yaml

# 调用函数 写个全局变量先 太典了家人们
result = load_yaml()

__plugin_name__ = result['Thanksto']['Name']
__plugin_usage__ = result['Thanksto']['Usage']


@on_command(result['Thanksto']['FirstKey'], aliases=result['Thanksto']['Aliases'])
async def _(session: CommandSession):
    await session.send(result['Thanksto']['Send'])