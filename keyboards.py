from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CITIES = {
    "Київ": "Kyiv",
    "Львів": "Lviv",
    "Одеса": "Odesa",
    "Харків": "Kharkiv",
    "Дніпро": "Dnipro"
}

def get_weather_keyboard():
    kb = InlineKeyboardMarkup(row_width=2)

    for city_ua, city_en in CITIES.items():
        kb.insert(InlineKeyboardButton(text=city_ua, callback_data=f"weather_{city_en}"))

    return kb