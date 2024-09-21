import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import API_TOKEN


default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)

bot = Bot(token=API_TOKEN, default=default_properties)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name}')


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда help ')


@dp.message(F.text.in_(['Финансы', 'Finance', 'Начать']))
async def finance_count(message: Message):
    await message.answer('Начинаю подсчитывать:')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())