from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class Reg(StatesGroup):
    f_name = State()
    s_name = State()
    id: int


reg_router = Router()

@reg_router.message(Command('reg'))
async def reg_first_name(message: Message, state: FSMContext):
    await state.set_state(Reg.f_name)
    await message.answer('Введите вашу Фамилию')


@reg_router.message(Reg.f_name)
async def reg_second_name(message: Message, state: FSMContext):
    await state.update_data(f_name=message.text)
    await state.set_state(Reg.s_name)
    await message.answer('Введите ваше Имя')


@reg_router.message(Reg.s_name)
async def reg_user_id(message: Message, state: FSMContext):
    await state.update_data(s_name=message.text)
    await state.update_data(id=message.from_user.id)
    data = await state.get_data()
    await message.answer(
        f'Регистрация прошла успешно.\nФамилия: {data["f_name"]}\nИмя: {data["s_name"]}\nId: {data["id"]}'
    )
    await state.clear()