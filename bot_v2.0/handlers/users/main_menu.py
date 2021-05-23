from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import admins, queue_to_communication, dict_to_communication
from keyboards.inline import main_menu
from keyboards.inline.callback_datas import go_to_main_callback, main_callback
from keyboards.inline.main_menu import go_main_menu

from loader import dp, bot

from handlers.users.tasting import client
from states import ConnectToAdmin


@dp.callback_query_handler(go_to_main_callback.filter(answer="yes"))
async def go_to_main_menu(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    # client = get_user_from_site(call.from_user.id)
    await call.answer()
    # await bot.send_message(call.from_user.id, f"Чим ми можемо бути корисні, {client.get_name()}? 😃",
    #                        reply_markup=main_menu)
    await bot.send_message(call.from_user.id, f"Чим ми можемо бути корисні, {call.from_user.full_name}? 😃",
                           reply_markup=main_menu)


@dp.callback_query_handler(main_callback.filter(tab="connect_to_admin"))
async def connect_to_admin(call: CallbackQuery, callback_data: dict):
    await call.answer()
    if call.from_user.id not in queue_to_communication:
        queue_to_communication.append(call.from_user.id)
        dict_to_communication[str(call.from_user.id)] = call.message
    await bot.send_message(call.from_user.id, "Зачейкате хвилинку під'єдную вільного менеджера до чату 😃")
    await sleep(3)
    await bot.send_message(call.from_user.id, "До чату під'єднано менеджера Магазину")
    await ConnectToAdmin.State_Admin.set()


@dp.message_handler(state=ConnectToAdmin.State_Admin)
async def message_to_admin(message: types.Message, state: FSMContext):
    print("+" * 20)
    print(queue_to_communication)
    if message.from_user.id != admins[0] and message.from_user.id in queue_to_communication:
        await bot.send_message(admins[0], message.text)
    elif message.from_user.id not in queue_to_communication:
        async with state.proxy() as data:
            data["message"] = message.text


@dp.message_handler()
async def message_admin_to_client(message: types.Message):
    print("-" *20 + "\n\n@dp.message_handler()\nasync def message_admin_to_client(message: types.Message):\n\n"+"-"*20)
    if message.from_user.id == admins[0] and message.text == "Завершити чат":
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.send_message(queue_to_communication[0],
                               "Чат з менеджером завершений, давайте передемо до головного меню)",
                               reply_markup=go_main_menu)
        del dict_to_communication[str(queue_to_communication[0])]
        del queue_to_communication[0]
    elif message.from_user.id == admins[0]:
        if len(queue_to_communication) > 0:
            await bot.send_message(queue_to_communication[0], message.text)
    else:
        await message.answer(message.text)
