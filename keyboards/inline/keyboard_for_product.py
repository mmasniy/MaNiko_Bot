from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import go_to_main_callback, img_callback

first_product = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

buy_PP = InlineKeyboardButton(
    text=f"Купити по предоплаті ✅",
    callback_data="buy:PP"
)

buy_COD = InlineKeyboardButton(
    text=f"Замовити з післяплатою ☑",
    callback_data="buy:COD"
)

show_other_products = InlineKeyboardButton(
    text="Хочу ще щось підібрати 😇",
    callback_data="buy:to_all_product"
)

go_to_main_menu = InlineKeyboardButton(
    text="Головне меню бота",
    callback_data=go_to_main_callback.new(
                answer="yes"
            )
)

first_product.add(buy_PP, buy_COD, show_other_products, go_to_main_menu)

first_product_other_img = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

other_img = InlineKeyboardButton(
    text="Додаткові фото",
    callback_data=img_callback.new(
                answer="other_img"
            )
)

first_product_other_img.add(other_img)
