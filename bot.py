import os
import asyncio
import  logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from get_weather import  get_weather
from  keybords import get_weather_keyboard

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(commands=['weather', 'start'])
async def send_weather_keyboard(message: Message):
    keyboard = get_weather_keyboard()
    await message.answer("Оберіть місто:", reply_markup=keyboard)


@dp.callback_query(lambda c: c.data.startswith('weather_'))
async def weather_callback_handler(callback_query: CallbackQuery):
    city = callback_query.data.split("_")[1]
    weather_info = await get_weather(city)

    await bot.send_message(callback_query.from_user.id, weather_info)
    await callback_query.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

