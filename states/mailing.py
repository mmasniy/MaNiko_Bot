from aiogram.dispatcher.filters.state import StatesGroup, State


class Mailing(StatesGroup):
    Start = State()
    Preparation = State()
    Send_spacial_offer = State()
