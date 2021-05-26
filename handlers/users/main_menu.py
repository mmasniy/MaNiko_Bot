from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InputFile

from data.config import admins, queue_to_communication, dict_to_communication, sale_product, i
from keyboards.inline import main_menu
from keyboards.inline.callback_datas import go_to_main_callback, main_callback
from keyboards.inline.keyboard_for_product import first_product, first_product_other_img
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
    await bot.send_message(call.from_user.id, f"Оберіть, що саме Вас цікавить. 👆")


@dp.callback_query_handler(main_callback.filter(tab="connect_to_admin"))
async def connect_to_admin(call: CallbackQuery, callback_data: dict):
    await call.answer()
    if call.from_user.id not in queue_to_communication:
        queue_to_communication.append(call.from_user.id)
        dict_to_communication[str(call.from_user.id)] = call.message
    # print(dict_to_communication[f'{call.from_user.id}'])
    await bot.send_message(admins[0], f"Вас було додано до чату з користувачем: "
                                      f"@{dict_to_communication[f'{call.from_user.id}']['chat']['username']}")
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
        await bot.send_message(message.from_user.id, f"Вибачте, але я не розумію, чим саме можу допомогти Вам. Оберіть "
                                                     f"відподний пункт нижще. Дякую) 😃")
        await bot.send_message(message.from_user.id, f"Чим ми можемо бути корисні, {message.from_user.full_name}? 😃",
                               reply_markup=main_menu)
        await bot.send_message(message.from_user.id, f"Оберіть, що саме Вас цікавить. 👆")


@dp.callback_query_handler(main_callback.filter(tab="show_promotional_offers"))
async def show_promotional_offers(call: CallbackQuery, callback_data: dict):
    await call.answer()
    await bot.send_message(call.from_user.id, "Розсилка була розпочата!")
    await bot.send_photo(call.from_user.id, photo=InputFile("/Users/mmasniy/Desktop/MaNiko_Bot/img/SALE.jpeg"))
    # await sleep(5)
    # await bot.send_message(call.from_user.id, f"{sale_product['1']['name']}\n"
    #                                           f"Ціна звичайна: {sale_product['1']['old_price']}\n"
    #                                           f"Ціна зі знижкою: {sale_product['1']['new_price']}\n"
    #                                           f"{sale_product['1']['charact']}\n"
    #                                           f"{sale_product['1']['about']}",
    #                        reply_markup=first_product)
    # await bot.send_photo(call.from_user.id, photo=InputFile(path_or_bytesio=sale_product['1']['img']),
    #                      reply_markup=first_product_other_img)

    for item in sale_product:
        print(item)
        # await sleep(5)
        await bot.send_message(call.from_user.id, f"{sale_product[str(item)]['name']}\n"
                                                  f"Ціна звичайна: {sale_product[str(item)]['old_price']}\n"
                                                  f"Ціна зі знижкою: {sale_product[str(item)]['new_price']}\n"
                                                  f"{sale_product[str(item)]['charact']}\n"
                                                  f"{sale_product[str(item)]['about']}",
                               reply_markup=first_product)
        await bot.send_photo(call.from_user.id, photo=InputFile(path_or_bytesio=sale_product[str(item)]['img']),
                             reply_markup=first_product_other_img)
