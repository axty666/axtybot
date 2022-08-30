from os import path

import nonebot
import bot_config


nonebot.init(bot_config)
# 第一个参数为插件路径，第二个参数为插件前缀（模块的前缀）
nonebot.plugin.load_plugins(
    path.join(path.dirname(__file__), 'bot_plugins'), 'bot_plugins')
# talk内容包
nonebot.plugin.load_plugins(
    path.join(path.dirname(__file__), 'bot_plugins/talk'), 'bot_plugins.talk')
# 11th
nonebot.plugin.load_plugins(
    path.join(path.dirname(__file__), 'bot_plugins/11th'), 'bot_plugins.11th')
# bor
nonebot.plugin.load_plugins(
    path.join(path.dirname(__file__), 'bot_plugins/bor'), 'bot_plugins.bor')
# MARYT
nonebot.plugin.load_plugins(
    path.join(path.dirname(__file__), 'bot_plugins/MARYT'), 'bot_plugins.MARYT')
# VANILO
nonebot.plugin.load_plugins(
    path.join(path.dirname(__file__), 'bot_plugins/VANILO'), 'bot_plugins.VANILO')


# 如果使用 asgi
bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    nonebot.run()