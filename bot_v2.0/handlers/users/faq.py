from aiogram.types import CallbackQuery, InputFile

from keyboards.inline.callback_datas import main_callback, faq_menu_callback
from keyboards.inline.faq_menu import faq_main_menu, about_us_menu, about_us_menu_second_level, delivery_methods_menu, \
    back_to_delivery_methods_menu_second_level, pay_methods_menu, back_to_pay_methods_menu_second_level, \
    return_product_menu
from loader import dp, bot


@dp.callback_query_handler(main_callback.filter(tab="show_faq"))
async def main_menu_faq(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id, f"Це наше меню з найпоширенішими питаннями. "
                                              f"{call.from_user.first_name}, виберіть групу, "
                                              f"яка може відповідати питанню, що у Вас виникло. ⁉",
                           reply_markup=faq_main_menu)
    photo = InputFile(path_or_bytesio="/Users/mmasniy/Desktop/MaNiko_Bot/img/faq-tbs-msc.png")
    await bot.send_photo(call.from_user.id, photo=photo)


# about_us way==========================================================================================================

@dp.callback_query_handler(faq_menu_callback.filter(subgroup="about_us", item="0"))
async def about_us_level_one(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f'Розділ "Про нас 🏡" несе інформацію про компанію та нашу діяльність. 🇺🇦',
                           reply_markup=about_us_menu)


@dp.callback_query_handler(faq_menu_callback.filter(subgroup="about_us", item="1"))
async def about_us_level_two(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f"Про магазин 🏡\nМи - компанія MaNiko, продаємо товари з Європи, "
                           f"зокрема з Німеччини, Нідерландів, Франції та Італії. "
                           f"Товари з магазину \"LIDL\". Якісні товари за доступною ціною. "
                           f"Працюємо напряму з компаніями-виробниками, тому можемо запропонувати "
                           f"своїм клієнтам вигідні та доступні ціни за європейську якість! "
                           f"Наша компанія працює як в роздрібній торгівлі, так і в оптовій, "
                           f"якщо є пропозиції про співпрацю - будемо раді обговорити! "
                           f"Ми завжди за зростання і розвиток!",
                           reply_markup=about_us_menu_second_level)


# about_us way==========================================================================================================

# delivery way==========================================================================================================

@dp.callback_query_handler(faq_menu_callback.filter(subgroup="delivery_methods", item="0"))
async def delivery_level_one(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f'Розділ "Способи доставки 📦" несе інформацію про всі '
                           f'можливі варіанти доставки замовлення до клієнта. 🚚',
                           reply_markup=delivery_methods_menu)


@dp.callback_query_handler(faq_menu_callback.filter(subgroup="delivery_methods", item="NP"))
async def delivery_level_two_np(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f"Доставка Новою Поштою відбувається того ж дня, "
                           f"як клієнт підтвердив замовлення. Компанія доставляє "
                           f"в сроки 1-3 дні. Є найбільшою компанією-перевізником "
                           f"в Україні. Середня вартість доставки 40-55 грн.",
                           reply_markup=back_to_delivery_methods_menu_second_level)


@dp.callback_query_handler(faq_menu_callback.filter(subgroup="delivery_methods", item="JS"))
async def delivery_level_two_js(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f"Доставка Justin відбувається по понеділкам, середам та п'ятницям. "
                           f"Компанія-перевізник активно розвивається та збільшує кількість "
                           f"відділень по Україні. Середня вартість доставки 30-45 грн.",
                           reply_markup=back_to_delivery_methods_menu_second_level)


@dp.callback_query_handler(faq_menu_callback.filter(subgroup="delivery_methods", item="KP"))
async def delivery_level_two_kp(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f"Доставка Kasta Post відбувається тогож дня, як улієнт сплатив "
                           f"або підтвердив замовлення. Компанія-перевізник активно збільшує "
                           f"кількість відділень по Україні. Сроки доставки 4-7 днів та вартість 29 грн.",
                           reply_markup=back_to_delivery_methods_menu_second_level)


@dp.callback_query_handler(faq_menu_callback.filter(subgroup="delivery_methods", item="self_pickup"))
async def delivery_level_two_self(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f"Самовивіз товару зі складу компанії відбувається в робочий час "
                           f"за адресою м.Київ, вул. Бориспільська, 7."
                           f"\n\nГрафік роботи магазину: "
                           f"\nПн-Пт - з 9 до 18 години"
                           f"\nСб - з 11 по 16 години"
                           f"\nНд - вихідний",
                           reply_markup=back_to_delivery_methods_menu_second_level)

# delivery way==========================================================================================================


# pay way===============================================================================================================

@dp.callback_query_handler(faq_menu_callback.filter(subgroup="pay_methods", item="0"))
async def pay_level_one(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f'Ви маєте змогу сплатити за замовленнями такими способами 👇',
                           reply_markup=pay_methods_menu)


@dp.callback_query_handler(faq_menu_callback.filter(subgroup="pay_methods", item="PP"))
async def pay_level_two_pp(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f"Сплатити на розрахунковий рахунок Ви можете за реквізитами, "
                           f"які надасть Вам менеджер при оформленні замовлення.",
                           reply_markup=back_to_pay_methods_menu_second_level)


@dp.callback_query_handler(faq_menu_callback.filter(subgroup="pay_methods", item="CC"))
async def pay_level_two_cc(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f"Сплата на картку Приват Банку відбувається по реквєзитам карти, "
                           f"які надасть менеджер при оформленні замоалення.",
                           reply_markup=back_to_pay_methods_menu_second_level)


@dp.callback_query_handler(faq_menu_callback.filter(subgroup="pay_methods", item="COD"))
async def pay_level_two_cod(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f"Сплата при отриманні відбувається на відділенні компанії-перевізника, "
                           f"коли клієнт отримує замовлення на руки. Відправка цим способом відбуваєть "
                           f"на замовлення, що мають суму 200 і більше гривень.",
                           reply_markup=back_to_pay_methods_menu_second_level)
# pay way===============================================================================================================


# return product way====================================================================================================

@dp.callback_query_handler(faq_menu_callback.filter(subgroup="return_product", item="0"))
async def return_product_level_one(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id,
                           f'Повернення товару відбувається в період 14-ти днів після отримання клієнтом посилки. '
                           f'Товар приймається, якщо він не був у використанні та має всі бірки та товарний вигляд.',
                           reply_markup=return_product_menu)
# return product way====================================================================================================
