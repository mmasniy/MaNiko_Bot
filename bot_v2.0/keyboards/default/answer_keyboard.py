from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ваш Контакт 📱", request_contact=True)
        ]
    ], resize_keyboard=True
)
