from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CITIES = {
    "Київ": "Kyiv",
    "Львів": "Lviv",
    "Одеса": "Odesa",
    "Харків": "Kharkiv",
    "Дніпро": "Dnipro",
    "Луцьк": "Lutsk",
    "Маріуполь": "Mariupol"
}


def get_weather_keyboard():
    buttons = [
        [InlineKeyboardButton(text=city_ua, callback_data=f"weather_{city_en}")]
        for city_ua, city_en in CITIES.items()
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_ua_city_name(city_en: str) -> str:
    for city_ua, city_eng in CITIES.items():
        if city_eng == city_en:
            return city_ua

    return city_en
