import requests
from datetime import datetime
from aiogram import Bot, Dispatcher, types, executor
from config import token_bot

bot = Bot(token_bot)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
   await bot.send_message(message.from_user.id, f'Привіт, {message.from_user.first_name}, вас вітає команда компанії '
                                                f'MaNiko! Чим ми могли б бути вам корисні?')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)