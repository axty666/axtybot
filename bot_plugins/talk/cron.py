import nonebot
import time
from datetime import datetime
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from .data_load import load_yaml

# 调用函数 写个全局变量先
result = load_yaml()

# 上午八点的提示
@nonebot.scheduler.scheduled_job('cron', hour=result['Crontime']['CronOne']['hour'], 
                                        minute=result['Crontime']['CronOne']['minute'])
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone(
        result['Crontime']['CronOne']['TimeZone']))
    try:
        await bot.send_group_msg(group_id=result['Crontime']['CronOne']['Group_id'],
                                message=result['Crontime']['CronOne']['Message'])
    except CQHttpError:
        pass

#上午九点的提示
@nonebot.scheduler.scheduled_job('cron', hour=result['Crontime']['CronTwo']['hour'], 
                                        minute=result['Crontime']['CronTwo']['minute'])
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone(
        result['Crontime']['CronTwo']['TimeZone']))
    try:
        await bot.send_group_msg(group_id=result['Crontime']['CronTwo']['Group_id'],
                                message=result['Crontime']['CronTwo']['Message'])
    except CQHttpError:
        pass

#下午三点的提示
@nonebot.scheduler.scheduled_job('cron', hour=result['Crontime']['CronThree']['hour'],
                                        minute=result['Crontime']['CronThree']['minute'])
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone(
        result['Crontime']['CronThree']['TimeZone']))
    try:
        await bot.send_group_msg(group_id=result['Crontime']['CronThree']['Group_id'],
                                message=result['Crontime']['CronThree']['Message'])
    except CQHttpError:
        pass

#下午11点的提示
@nonebot.scheduler.scheduled_job('cron', hour=result['Crontime']['CronFour']['hour'],
                                        minute=result['Crontime']['CronFour']['minute'])
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone(
        result['Crontime']['CronFour']['TimeZone']))
    try:
        await bot.send_group_msg(group_id=result['Crontime']['CronFour']['Group_id'],
                                message=result['Crontime']['CronFour']['Message'])
    except CQHttpError:
        pass
