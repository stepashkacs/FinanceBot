import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import API_TOKEN
from app.handlers import router

default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)

bot = Bot(token=API_TOKEN, default=default_properties)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())