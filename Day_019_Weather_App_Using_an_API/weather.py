import os
import requests
from dotenv import load_dotenv

load_dotenv()

city = input("City: ").strip()

key = os.getenv("OPENWEATHER_API_KEY")
url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q" : city , "appid" : key, "unit" : "metric"}

try:
    responce = requests.get(url,params=params,timeout=10)
    responce.raise_for_status()
    data = responce.json()
    print(f"{data['name']} : {data['main']}['temp'] C")
    print(data["weather"][0]["descroption".title()])
except requests.RequestException as error:
    print(f"Weather request failed: {error}")    