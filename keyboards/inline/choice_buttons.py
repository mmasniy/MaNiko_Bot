from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import meet_callback

site = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Сайт нашого магазину 🎆",
                             url="https://maniko.com.ua")
    ]
])

choice = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text="Давай знайомитись 😉", callback_data=meet_callback.new(answer="yes")),
        InlineKeyboardButton(text="Ні, не маю бажання 😁", callback_data=meet_callback.new(answer="no"))
    ]
])