import requests
from datetime import datetime
from aiogram import Bot, Dispatcher, types, executor
from config import token_bot, answer_first_layer, id_admins
from database import BotSQl

def create_markup(keys_list):
    answer = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    answer.add(keys_list[0])
    answer.add(keys_list[1])
    answer.add(keys_list[2])
    answer.add(keys_list[3])
    return answer