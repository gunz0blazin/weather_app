###This is a test file for calling a weather api 

import datetime as datetime
import requests
import os 
from dotenv import load_dotenv


load_dotenv() #load .env file

#breakout openweathermap geocoding api url: https://openweathermap.org/api/geocoding-api
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = os.getenv("openweather_api")
city = input("City:").capitalize()

#this is the formula for the api url
test_url = base_url + "q=" + city + "&limit=5&appid=" + api_key + "&units=metric"

#.json() needed to format to a pyton dict refer to requests docs for more: https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
raw_data = requests.get(test_url).json()
if raw_data.get('cod') != 200:
    print("Error:", raw_data.get("message", "Unknown error"))
    exit()
#print(raw_data)


#get usefull readings from api 
tempC= raw_data["main"]["temp"]
humidity= raw_data["main"]["humidity"]
description=raw_data["weather"][0]["description"]
name=raw_data["name"]


print(f"""
Weather Report for {name}:

Temperature: {tempC}°C
Humidity: {humidity}%
Condition: {description}
""")

#Todo 
#get a a DB going(influx?)
#connect api server to DB

