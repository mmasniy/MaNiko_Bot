from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import main_callback
from loader import dp, bot


@dp.callback_query_handler(main_callback.filter(tab="show_faq"))
async def main_menu_faq(call: CallbackQuery):
    await call.answer()
    await bot.send_message(call.from_user.id, f"Це наше меню з найпоширенішими питаннями. "
                                              f"{call.from_user.first_name}, виберіть групу, "
                                              f"яка може відповідати питанню, що у Вас виникло. ⁉",
                           reply_markup=faq_main_menu)
