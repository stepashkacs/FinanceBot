from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F


from app.keyboards import main_kb, aboutme_kb, products_kb


user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name} \nТвой id: {message.from_user.id}',
                         reply_markup=main_kb.main)


@user_router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда help ')


@user_router.message(F.text.in_(['Финансы', 'Finance', 'Начать']))
async def finance_count(message: Message):
    await message.answer('Начинаю подсчитывать:')


@user_router.message(F.text == 'Обо мне')
async def about_me(message: Message):
    await message.reply(
        'Мои Контакты',
        reply_markup=aboutme_kb.about_me,
    )


@user_router.message(F.text == 'Продукты')
async def products(message: Message):
    await message.answer('Выберите категорию:',
                         reply_markup=products_kb.products)


@user_router.callback_query(F.data == 'sneakers')
async def sneakers(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Вы выбрали категорию Кросовок')


@user_router.callback_query(F.data == 't-shirts')
async def sneakers(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Вы выбрали категорию Футболок')


@user_router.callback_query(F.data == 'pants')
async def sneakers(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Вы выбрали категорию Штанов')