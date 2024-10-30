from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью')


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите ваш возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message):
    await message.answer('Введите ваш рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message):
    await message.answer('Введите ваш вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    await state.update_data(age=message.text)
    await state.update_data(growth=message.text)
    data = await state.get_data()
    calories_for_woman = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    calories_for_men = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Для женщин от 13 до 80 лет норма калорий - {calories_for_woman} ккал\nДля мужчин от 13 до '
                         f'80 лет норма калорий - {calories_for_men} ккал')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
