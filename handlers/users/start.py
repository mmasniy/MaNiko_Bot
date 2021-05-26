from asyncio import sleep

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from loader import dp, bot
from keyboards.inline.choice_buttons import site
from keyboards.inline.choice_buttons import choice
from keyboards.inline.callback_datas import meet_callback


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Доброго дня, Вас вітає магазин MaNiko, де Ви можете придбати товари для дому, "
                         f"декор та одяг! Будемо раді нашій співпраці)\n\n"
                         f"Це наш віртуальний помічник, що допоможе Вам підтримувати зв'язок з нами. "
                         f"Також у нас є сайт, де також можна прибати всі товари) 🆕", reply_markup=site)
    await sleep(1)
    await message.answer(f"Ми маємо бажання з Вами познайомитись, "
                         f"щоб маnb змогу бути завжди на зв'язку. "
                         f"Також у виногороду надати Вам знижку на перше замовлення) "
                         f"Ми раді, що Ви завітали до нас!", reply_markup=choice)

