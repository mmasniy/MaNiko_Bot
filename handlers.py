from main import bot, dp
from aiogram import types
from config import answer_first_layer, id_admins
from database import BotSQl
import functions
import config
import asyncio

async def send_message_to_admin(dp):
    for admin in id_admins:
        await bot.send_message(chat_id=admin, text="Новий користувач в нашому боті!")
