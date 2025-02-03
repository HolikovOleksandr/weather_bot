from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CITIES = {
    "Київ": "Kyiv",
    "Львів": "Lviv",
    "Одеса": "Odesa",
    "Харків": "Kharkiv",
    "Дніпро": "Dnipro"
}


def get_weather_keyboard():
    buttons = [
        [InlineKeyboardButton(text=city_ua, callback_data=f"weather_{city_en}")]
        for city_ua, city_en in CITIES.items()
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
