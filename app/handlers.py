from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, F

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name} \nТвой id: {message.from_user.id}',
                         reply_markup=kb.main)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда help ')


@router.message(F.text.in_(['Финансы', 'Finance', 'Начать']))
async def finance_count(message: Message):
    await message.answer('Начинаю подсчитывать:')


@router.message(F.text == 'Обо мне')
async def about_me(message: Message):
    await message.reply('Мой Контакты',
        reply_markup=kb.about_me
    )
