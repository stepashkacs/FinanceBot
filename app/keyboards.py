from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Мои Финансы'), KeyboardButton(text='Мои Активы',)],
    [KeyboardButton(text='Новые Финансы')],
    [KeyboardButton(text='Обо мне')],
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт пеню'
)

about_me = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Мои GitHub', url='https://github.com/stepashkacs')],
        [InlineKeyboardButton(text='Мои Instagram', url='https://www.instagram.com/__stefan__c__/')],
        [InlineKeyboardButton(text='Мои Steam', url='https://steamcommunity.com/profiles/76561199082071769/')],

    ]
)