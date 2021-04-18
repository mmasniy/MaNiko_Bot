import requests
from datetime import datetime
from aiogram import Bot, Dispatcher, types, executor
from config import token_bot, answer_first_layer, id_admins

bot = Bot(token_bot)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    print(message.from_user.id)

    print(f'Нам пишет {message.from_user.full_name}')

    answer = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    answer.add(answer_first_layer[0])
    answer.add(answer_first_layer[1])
    answer.add(answer_first_layer[2])
    answer.add(answer_first_layer[3])

    # if message.from_user.id == 669655144:
    #     await bot.send_message(message.from_user.id, 'Я слежу за тобой))')
    # else:
    await bot.send_message(message.from_user.id, f'Привіт, {message.from_user.first_name}, '
                                                 f'вас вітає команда компанії MaNiko! Чим ми можемо бути корисні?',
                           reply_markup=answer
                           )


@dp.message_handler(content_types=['text'])
async def answer_message_first_layer(message: types.Message):
    if message.text == answer_first_layer[0]:
        await bot.send_message(id_admins[0], "-" * 100 +
                                             f"\nКлієнт хоче замовити товар, зв'яжись з ним! "
                                             f"@{message.from_user.username}\n" + "-" * 100)
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, менеджери отримали ваше "
                                                     f"звернення, вони зв'яжуться з вами якнайшвидше!")
    elif message.text == answer_first_layer[1]:
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, вас було додано до"
                                                     f" розсилки акційних пропозицій!")
        print(f'Add to Sales messages {message.from_user.full_name}!')
    elif message.text == answer_first_layer[2]:
        await bot.send_message(id_admins[0], f"-" * 100 +
                                             f"\nКлієнт хоче повернути товар, зв'яжись з ним! "
                                             f"@{message.from_user.username}\n" + "-" * 100)
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, менеджери отримали ваше "
                                                     f"звернення, вони зв'яжуться з вами якнайшвидше!")
    elif message.text == answer_first_layer[3]:
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, додавання цього функціоналу"
                                                     f" буде найближчим часом! Ми обов'язково повідомимо про це!")
    else:
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, нажаль, я не розумію, "
                                                     f"чим ми можемо вам допопмогти, виберіть, будь-ласка, відповідь"
                                                     f" серед кнопок. Дякую!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)

# """ ID-users
# 669655144 - Vika
# 327677748 - Tima Bratslavskyi
# 188545439 - Maksim Masniy
# 530420596 - Павел
# """
