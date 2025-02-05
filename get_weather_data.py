import os
import aiohttp

async def get_weather_data(city: str):
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            if response.status == 200:
                weather_data = {
                    "temp": data["main"]["temp"] - 273.15,
                    "feels": data["main"]["feels_like"] - 273.15,
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"]
                }

                return weather_data
            else:
                return "Не вдалося отримати дані про погоду. Спробуйте пізніше."
