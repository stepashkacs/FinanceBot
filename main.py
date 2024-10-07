import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os

from app.handlers.user_handler import user_router
from app.handlers.user_reg import reg_router


load_dotenv()


async def main():
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=os.getenv('API_TOKEN'), default=default_properties)
    dp = Dispatcher()
    dp.include_router(user_router)
    dp.include_router(reg_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')