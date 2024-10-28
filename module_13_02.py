from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7922011700:AAGARiPWVtHGtn8ZZiFZ0hgXoxf3tMx5a_Y"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    #await message.answer('Привет, я бот!')


@dp.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.")
    #await message.answer('Я бот, который поможет тебе!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
