import requests
import json

city = "pomerode"
country = "Brasil"

api_key = "7f892615b6d76dde516d3d6ea6a11147"

weather_url = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=metric')

weather_data = weather_url.json()