import nonebot
import time
from datetime import datetime
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
Groups = [640614812, 691790710, 591948356]

#上午八点的提示
@nonebot.scheduler.scheduled_job('cron', hour='8', minute='0')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=640614812,
                             message="八点整力，劲爆激情尽在麦瑞")
    except CQHttpError:
        pass

#上午九点的提示
@nonebot.scheduler.scheduled_job('cron', hour='9', minute='0')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=640614812,
                             message="你醒啦，该上m服签到力")
    except CQHttpError:
        pass

#下午三点的提示
@nonebot.scheduler.scheduled_job('cron', hour='15', minute='0')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=640614812,
                             message="三点力！该摸服力！")
    except CQHttpError:
        pass

#下午11点的提示
@nonebot.scheduler.scheduled_job('cron', hour='23', minute='0')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=640614812,
                             message="十一点咯，夜深了，放下书摸会麦瑞放放松好不好")
    except CQHttpError:
        pass
