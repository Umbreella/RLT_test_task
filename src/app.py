from aiogram import Bot, Dispatcher

from src.config import settings
from src.db import db
from src.routers import base, payment

bot = Bot(token=settings.TELEGRAM_ACCESS_TOKEN)


async def run():
    await db.init_db()
    await bot.set_my_commands(commands=[])

    dispatcher = Dispatcher()
    dispatcher.include_router(base.router)
    dispatcher.include_router(payment.router)

    await dispatcher.start_polling(bot)
