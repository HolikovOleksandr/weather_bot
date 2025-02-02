import os
import aiohttp

async def get_weather(city: str):
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            if response.status == 200:
                weather_description = data['weather'][0]['description']
                temp = data['main']['temp'] - 273.15
                return f"Погода в {city}: {temp:.2f}°C"
            else:
                return "Не вдалося отримати дані про погоду. Спробуйте пізніше."
