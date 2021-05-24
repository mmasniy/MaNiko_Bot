from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import faq_menu_callback, go_to_main_callback, main_callback

# faq_main_menu__________________________________________________________
faq_main_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

about_us = InlineKeyboardButton(
    text=f"Про нас 🏡",
    callback_data=faq_menu_callback.new(
        subgroup="about_us",
        item="0"
    )
)

delivery_methods = InlineKeyboardButton(
    text="Способи доставки 📦",
    callback_data=faq_menu_callback.new(
        subgroup="delivery_methods",
        item="0"
    )
)

pay_methods = InlineKeyboardButton(
    text="Способи оплати 💸",
    callback_data=faq_menu_callback.new(
        subgroup="pay_methods",
        item="0"
    )
)

return_product = InlineKeyboardButton(
    text="Повернення товару 📤",
    callback_data=faq_menu_callback.new(
        subgroup="return_product",
        item="0"
    )
)

go_to_menu = InlineKeyboardButton(
    text="Назад до головного меню 👈",
    callback_data=go_to_main_callback.new(
        answer="yes"
    )
)

faq_main_menu.add(about_us, delivery_methods, pay_methods, return_product, go_to_menu)
# faq_main_menu__________________________________________________________

# faq_main_menu->about_us________________________________________________

about_us_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

about_shop = InlineKeyboardButton(
    text=f"Про магазин 🏡",
    callback_data=faq_menu_callback.new(
        subgroup="about_us",
        item="1"
    )
)

go_to_faq_main_menu = InlineKeyboardButton(
    text="Поширені запитання FAQ 😉",
    callback_data=main_callback.new(
        tab="show_faq"
    )
)

about_us_menu.add(about_shop, go_to_faq_main_menu, go_to_menu)
# faq_main_menu->about_us________________________________________________


# faq_main_menu->delivery_methods________________________________________

delivery_methods_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

about_NP = InlineKeyboardButton(
    text=f"Нова Пошта 🟥",
    callback_data=faq_menu_callback.new(
        subgroup="delivery_methods",
        item="NP"
    )
)

about_JS = InlineKeyboardButton(
    text=f"Justin 🟦",
    callback_data=faq_menu_callback.new(
        subgroup="delivery_methods",
        item="JS"
    )
)

about_KP = InlineKeyboardButton(
    text=f"Kasta Post ⬛",
    callback_data=faq_menu_callback.new(
        subgroup="delivery_methods",
        item="KP"
    )
)

self_pickup = InlineKeyboardButton(
    text=f"Самовивіз зі складцу компанії 🏢",
    callback_data=faq_menu_callback.new(
        subgroup="delivery_methods",
        item="self_pickup"
    )
)

delivery_methods_menu.add(about_NP, about_JS, about_KP, self_pickup, go_to_faq_main_menu, go_to_menu)
# faq_main_menu->delivery_methods________________________________________

# faq_main_menu->pay_methods_____________________________________________

pay_methods_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

pay_to_PP = InlineKeyboardButton(
    text=f"Сплата по реквізитам на розрахунковий рахунок",
    callback_data=faq_menu_callback.new(
        subgroup="pay_methods",
        item="PP"
    )
)

pay_to_CC = InlineKeyboardButton(
    text=f"Сплата на картку Приват Банку",
    callback_data=faq_menu_callback.new(
        subgroup="pay_methods",
        item="CC"
    )
)

C_O_D = InlineKeyboardButton(
    text=f"Сплата при отриманні товару",
    callback_data=faq_menu_callback.new(
        subgroup="pay_methods",
        item="COD"
    )
)

pay_methods_menu.add(pay_to_PP, pay_to_CC, C_O_D, go_to_faq_main_menu, go_to_menu)
# faq_main_menu->delivery_methods________________________________________

# faq_main_menu->return_product__________________________________________

return_product_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

return_product_menu.add(go_to_faq_main_menu, go_to_menu)
# faq_main_menu->return_product__________________________________________


# keyboard_for_second_level_subgroups____________________________________

about_us_menu_second_level = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

back_to_about_us_menu = InlineKeyboardButton(
    text=f"Назад до категорії 'Про нас 🏡'",
    callback_data=faq_menu_callback.new(
        subgroup="about_us",
        item="0"
    )
)

about_us_menu_second_level.add(back_to_about_us_menu, go_to_faq_main_menu, go_to_menu)

back_to_delivery_methods_menu_second_level = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

back_to_delivery_methods_menu = InlineKeyboardButton(
    text=f"Розділ доставки",
    callback_data=faq_menu_callback.new(
        subgroup="delivery_methods",
        item="0"
    )
)

back_to_delivery_methods_menu_second_level.add(back_to_delivery_methods_menu, go_to_faq_main_menu, go_to_menu)

back_to_pay_methods_menu_second_level = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

back_to_pay_methods_menu = InlineKeyboardButton(
    text=f"Розділ 'Способи оплати'",
    callback_data=faq_menu_callback.new(
        subgroup="pay_methods",
        item="0"
    )
)

back_to_pay_methods_menu_second_level.add(back_to_pay_methods_menu, go_to_faq_main_menu, go_to_menu)

# keyboard_for_second_level_subgroups____________________________________
