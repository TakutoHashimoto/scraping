import requests
import json
import os

OPEN_WEATHER_MAP_API_KEY = os.environ.get('OPEN_WEATHER_MAP_API_KEY')
# print(OPEN_WEATHER_MAP_API_KEY)

# 現在の東京の天気を取得する
url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"

url = url.format(city="Tokyo,JP", key=OPEN_WEATHER_MAP_API_KEY)

json_data = requests.get(url).json()
print(json_data)
