from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


about_me = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Мои GitHub', url='https://github.com/stepashkacs')],
        [InlineKeyboardButton(text='Мои Instagram', url='https://www.instagram.com/__stefan__c__/')],
        [InlineKeyboardButton(text='Мои Steam', url='https://steamcommunity.com/profiles/76561199082071769/')],

    ]
)
