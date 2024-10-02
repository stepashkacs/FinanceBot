from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


products = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Кросовки', callback_data='sneakers')],
        [InlineKeyboardButton(text='Футболки', callback_data='t-shirts')],
        [InlineKeyboardButton(text='Штаны', callback_data='pants')],

    ]
)