from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.config import dict_to_communication, queue_to_communication
from loader import dp, bot

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from states.for_admins import Admin


@dp.message_handler(Command("close_chat"))
async def close_chat(message: types.Message):
    await Admin.Close_chat.set()
    await message.answer("Оберіть id-юзера, чат з яким потрібно закрити:", reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(f"{dict_to_communication[str(queue_to_communication[0])]}")
            ]
        ], resize_keyboard=True
    ))
    # дописать функу с завершением чата


@dp.message_handler(state=Admin.Close_chat)
async def close_choose_chat(message: types.Message):
    bot.send_message(queue_to_communication[0], "Чат з менеджером був закінченим, дякуємо за співпрацю!")
