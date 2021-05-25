from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import meet_callback
from keyboards.inline.faq_menu import go_to_menu

from data.config import dict_to_communication, queue_to_communication

# buttons after cancel chat with admin for client ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

cancel_chat = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])

site = InlineKeyboardButton(text="Сайт нашого магазину 🎆", url="https://maniko.com.ua")

cancel_chat.add(site, go_to_menu)
# buttons after cancel chat with admin for client ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # buttons for admin before selection chat, which to need tp close ++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# choice_chat = InlineKeyboardMarkup(row_width=1, inline_keyboard=[])
#
# if len(queue_to_communication) > 1:
#     chat1 = InlineKeyboardButton(text=f"{dict_to_communication[f'{queue_to_communication[0]}']['chat']['id']} - "
#                                       f"{dict_to_communication[f'{queue_to_communication[0]}']['chat']['username']}")
#     choice_chat.add(chat1)
#
# if len(queue_to_communication) > 2:
#     chat2 = InlineKeyboardButton(text=f"{dict_to_communication[f'{queue_to_communication[1]}']['chat']['id']} - "
#                                       f"{dict_to_communication[f'{queue_to_communication[1]}']['chat']['username']}")
#     choice_chat.add(chat2)
#
# # buttons for admin before selection chat, which to need tp close ++++++++++++++++++++++++++++++++++++++++++++++++++++++
