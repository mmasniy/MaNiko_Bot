from asyncio import sleep

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery, InputFile, MediaGroup

from data.config import dict_to_communication, queue_to_communication, admins, sale_product, i
from keyboards.inline.admin_buttons import cancel_chat
from keyboards.inline.callback_datas import go_to_main_callback, mail_callback, img_callback
from keyboards.inline.faq_menu import go_to_menu
from keyboards.inline.keyboard_for_product import first_product, first_product_other_img
from loader import dp, bot

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from states.for_admins import Admin
from states.mailing import Mailing


@dp.message_handler(Command("close_chat"))
async def close_chat(message: types.Message):
    await Admin.Close_chat.set()
    user = dict_to_communication[str(queue_to_communication[0])]
    await message.answer("Оберіть id-юзера, чат з яким потрібно закрити:",
                         reply_markup=InlineKeyboardMarkup(row_width=1, inline_keyboard=[
                             [
                                 InlineKeyboardButton(
                                     text=f"{dict_to_communication[f'{queue_to_communication[0]}']['chat']['id']} - "
                                          f"{dict_to_communication[f'{queue_to_communication[0]}']['chat']['username']}",
                                     callback_data=go_to_main_callback.new(
                                         answer=f'{queue_to_communication[0]}'
                                     )
                                 )
                             ]]))


@dp.callback_query_handler(state=Admin.Close_chat)
async def close_choose_chat(call: CallbackQuery):
    await call.answer()
    await dp.storage.wait_closed()
    # await dp.storage.wait_closed()
    await bot.send_message(admins[0], "Чат з клієнтом було завершено!")
    await bot.send_message(queue_to_communication[0], "Чат з менеджером був закінченим, дякуємо за співпрацю!",
                           reply_markup=cancel_chat)
    del dict_to_communication[str(queue_to_communication[0])]
    del queue_to_communication[0]


@dp.message_handler(user_id=admins[0], commands=["promo_mail"])
async def start_promo_mail(message: types.Message):
    # await Mailing.Start().set()
    await message.answer("Розпочати розсилку по клієнтам?",
                         reply_markup=InlineKeyboardMarkup(row_width=1, inline_keyboard=[
                             [
                                 InlineKeyboardButton(
                                     text="Да, розпочати зараз",
                                     callback_data=mail_callback.new(
                                         answer="yes"
                                     )
                                 )
                             ],
                             [
                                 InlineKeyboardButton(
                                     text="Ні, повернутись до головного меню",
                                     callback_data=go_to_main_callback.new(
                                         answer="yes"
                                     )
                                 )
                             ]]))


@dp.callback_query_handler(mail_callback.filter(answer="yes"))
async def prepare_promo_email(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id, "Розсилка була розпочата!")
    await bot.send_photo(call.from_user.id, photo=InputFile("/Users/mmasniy/Desktop/MaNiko_Bot/img/SALE.jpeg"))
    await sleep(5)
    i.append(1)
    await bot.send_message(call.from_user.id, f"{sale_product['1']['name']}\n"
                                              f"Ціна звичайна: {sale_product['1']['old_price']}\n"
                                              f"Ціна зі знижкою: {sale_product['1']['new_price']}\n"
                                              f"{sale_product['1']['charact']}\n"
                                              f"{sale_product['1']['about']}",
                           reply_markup=first_product)
    await bot.send_photo(call.from_user.id, photo=InputFile(path_or_bytesio=sale_product['1']['img']),
                         reply_markup=first_product_other_img)
    # for item in sale_product:

    # await bot.send_message(call.from_user.id, f"{call.from_user.first_name}, Вас було додано до акційної розсилки"
    #                                           f" товарів! Кожного дня наш буде надсилати Вам товари зі знижкою або"
    #                                           f" товари, що мають великий попит серед покупців!"
    #                                           f" Дякуємо, що ви з нами) 😀", reply_markup=)


@dp.callback_query_handler(img_callback.filter(answer="other_img"))
async def send_other_photo(call: CallbackQuery):
    if len(i) == 0:
        other = sale_product[str(1)]['other_img'].split(";")
    else:
        other = sale_product[str(len(i))]['other_img'].split(";")
    for item in other:
        await bot.send_photo(call.from_user.id, photo=InputFile(path_or_bytesio=item))
