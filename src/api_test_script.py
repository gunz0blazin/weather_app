###This is a test file for calling a weather api 

import datetime as datetime
import requests
import os 
from dotenv import load_dotenv


load_dotenv() #load .env file

#breakout openweathermap geocoding api url: https://openweathermap.org/api/geocoding-api
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = os.getenv("openweather_api")
city = "Columbus"

#this is the formula for the api url
test_url = base_url + "q=" + city + "&limit=5&appid=" + api_key

#.json() needed to format to a pyton dict refer to requests docs for more: https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
respose_test = requests.get(test_url).json()
print(respose_test)

#Todo 
#GET THE API KEYS OUT OF THE CODE BEFORE GIT ADD
#format data into usefull vars to play with or maybe breakout a smaller local dict
    #convert the kevin to C and F 
    #current humid
    #current temps
    #current cloud discription
    #name of city

#get a a DB going(influx?)
#connect api server to DB

