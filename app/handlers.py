from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, F

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name}')


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда help ')


@router.message(F.text.in_(['Финансы', 'Finance', 'Начать']))
async def finance_count(message: Message):
    await message.answer('Начинаю подсчитывать:')