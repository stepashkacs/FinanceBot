from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


import app.keyboards as kb


router = Router()


class Reg(StatesGroup):
    f_name = State()
    s_name = State()
    id: int


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



@router.message(Command('reg'))
async def reg_first_name(message: Message, state: FSMContext):
    await state.set_state(Reg.f_name)
    await message.answer('Введите вашу Фамилию')


@router.message(Reg.f_name)
async def reg_second_name(message: Message, state: FSMContext):
    await state.update_data(f_name=message.text)
    await state.set_state(Reg.s_name)
    await message.answer('Введите ваше Имя')


@router.message(Reg.s_name)
async def reg_user_id(message: Message, state: FSMContext):
    await state.update_data(s_name=message.text)
    await state.update_data(id=message.from_user.id)
    data = await state.get_data()
    await message.answer(
        f'Регистрация прошла успешно.\nФамилия: {data["f_name"]}\nИмя: {data["s_name"]}\nId: {data["id"]}'
    )
    await state.clear()