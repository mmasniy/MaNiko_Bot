from aiogram.utils.callback_data import CallbackData

meet_callback = CallbackData("meet", "answer")

main_callback = CallbackData("menu", "tab")

go_to_main_callback = CallbackData("go_to_main", "answer")

faq_menu_callback = CallbackData("faq_menu", "subgroup", "item")
