from aiogram.dispatcher.filters.state import StatesGroup, State


class GreetingTest(StatesGroup):
    Q1_name = State()
    Q2_phone = State()
    Q3_email = State()
