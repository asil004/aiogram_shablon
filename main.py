import asyncio
import logging
import os
import sys

from aiogram import Dispatcher, Bot, Router, types
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from dotenv import load_dotenv
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from routers import router as all_routers

load_dotenv('.env')

router = Router()
router.include_router(all_routers)

dbname = os.getenv('DBNAME')
dbuser = os.getenv('DBUSER')
dbpassword = os.getenv('DBPASSWORD')
SUPER_ADMIN = int(os.getenv('ADMIN'))

dp = Dispatcher()


async def main() -> None:
    # scheduler = AsyncIOScheduler(timezone='Asia/Tashkent')
    # scheduler.add_job(ud.get_update_db, trigger='cron', hour="00", minute=1)
    # scheduler.start()

    dp.include_router(router)
    bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
    commands = [
        BotCommand(command='start', description='Botni ishga tushurish ♻')
    ]
    # await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except [KeyboardInterrupt, SystemExit] as exp:
        logging.info('Bot stopped!')
