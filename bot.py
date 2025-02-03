import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from get_weather import get_weather
from keyboards import get_weather_keyboard  # Виправив ім'я модуля!

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)


@router.message(Command("start"))
@router.message(Command("weather"))
async def send_weather_keyboard(message: Message):
    keyboard = get_weather_keyboard()
    await message.answer("Оберіть місто:", reply_markup=keyboard)


@router.callback_query(F.data.startswith('weather_'))
async def weather_callback_handler(callback_query: CallbackQuery):
    city = callback_query.data.split("_")[1]
    weather_info = await get_weather(city)

    await callback_query.message.answer(weather_info)
    await callback_query.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
