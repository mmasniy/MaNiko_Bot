from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import main_callback, go_to_main_callback

# go to main menu
# ------------------------------------------------------------------

go_main_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Перейти до головного меню",
            callback_data=go_to_main_callback.new(
                answer="yes"
            )
        )
    ]
])
# ------------------------------------------------------------------


# main_menu and all buttons
# ------------------------------------------------------------------

main_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

connect_to_admin = InlineKeyboardButton(
    text=f"Зв'язатись з менеджером для замовлення товару 🆕",
    callback_data=main_callback.new(
        tab="connect_to_admin"
    )
)

show_promotional = InlineKeyboardButton(
    text="Показати акційні пропозиції 💸",
    callback_data=main_callback.new(
        tab="show_promotional_offers"
    )
)

faq = InlineKeyboardButton(
    text="Поширені запитання FAQ 😉",
    callback_data=main_callback.new(
        tab="show_faq"
    )
)

main_menu.add(connect_to_admin, show_promotional, faq)
# -------------------------------------------------------------------
