import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from get_weather_data import get_weather_data
from keyboards import get_weather_keyboard, get_ua_city_name

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
    city_en = callback_query.data.split("_")[1]
    city_ua = get_ua_city_name(city_en)

    data = await get_weather_data(city_en)
    weather = (
        f"*📍 Погода в місті {city_ua}*\n\n"
        f"🌡️ Температура: *{data['temp']:.1f}°C*\n"
        f"😓 Відчувається як: *{data['feels']:.1f}°C*\n"
        f"💧 Вологість: *{data['humidity']}%*\n"
        f"🌬️ Швидкість вітру: *{data['wind_speed']} м/с*"
    )

    await callback_query.message.edit_text(
        reply_markup=get_weather_keyboard(),
        parse_mode='Markdown',
        text=weather
    )

    await callback_query.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
