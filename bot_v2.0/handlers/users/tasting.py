from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.default import phone_number
from keyboards.inline.callback_datas import meet_callback
from keyboards.inline.main_menu import go_main_menu
from loader import dp, bot
from aiogram import types

from states import GreetingTest
from utils import ClientUser

client = None


@dp.callback_query_handler(meet_callback.filter(answer="yes"))
async def get_answer_yes(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer()
    await bot.send_message(call.from_user.id, "Напишіть Ваше ім'я 😉: ")
    await GreetingTest.Q1_name.set()


@dp.message_handler(state=GreetingTest.Q1_name)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["name"] = answer
    await message.answer(f"Для підтримки зв'язку введіть, будь-ласка, "
                         f"свій номер телефону в форматі +38(0**)***-**-** 😁 "
                         f"або натисніть кнопку нижче для відправки Вашого контаку.", reply_markup=phone_number)
    await GreetingTest.Q2_phone.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=GreetingTest.Q2_phone)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.contact.phone_number
    async with state.proxy() as data:
        data["phone"] = answer

    await message.answer(f"Також для зв'язку введіть свій email, будемо дуже вдячні! 😉",
                         reply_markup=ReplyKeyboardRemove())
    await GreetingTest.Q3_email.set()


@dp.message_handler(state=GreetingTest.Q3_email)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["email"] = answer

    data = await state.get_data()
    client = ClientUser(message.from_user.id, data.get("name"), data.get("phone"), data.get("email"))
    client.set_mailing(True)
    client.set_sale(15)
    # client.send_data_to_site()

    await message.answer(f"Дякуємо вам за ваш час та увагу! "
                         f"Дані зберено, в майбутньому ми завжди зможемо підтримувати зв'язок) ✨ "
                         f"Також за вами закріплена знижка в 15% на перше замаолення!  😉", reply_markup=go_main_menu)


@dp.callback_query_handler(meet_callback.filter(answer="no"))
async def get_answer_yes(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer()
    await bot.send_message(call.from_user.id, f"Тоді давайте перейдемо до головного меню нашого бота 😉",
                           reply_markup=go_main_menu)

    client = ClientUser(call.from_user.id, call.from_user.full_name, None, None)
    # client.send_data_to_site()
