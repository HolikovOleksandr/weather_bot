import asyncio
import os
import  logging
from get_weather import  get_weather
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(lambda msg: msg.text.lower() == '/start')
async def start_handler(msg: Message):
    await msg.answer("🤖Привіт! Я твій бот!")

@dp.message(lambda msg: msg.text.lower() == "/help")
async  def help_handler(msg: Message):
    await msg.answer("👨‍💻Ось доступні команди:\n/start - почати роботу з ботом\n/help - допомога\n/weather - погода в Київі")

@dp.message(lambda msg: msg.text.lower() == '/weather')
async  def weather_handler(msg: Message):
    weather_info = await get_weather('Kyiv')
    print(weather_info.upper())
    await msg.answer(weather_info)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

