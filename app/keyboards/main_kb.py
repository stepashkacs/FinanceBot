from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Мои Финансы'), KeyboardButton(text='Мои Активы',)],
    [KeyboardButton(text='Новые Финансы'), KeyboardButton(text='Продукты')],
    [KeyboardButton(text='Обо мне')],

],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт пеню'
)