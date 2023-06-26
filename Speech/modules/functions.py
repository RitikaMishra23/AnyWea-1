
import numpy as np
import os
import modules.speech as speech
import time
import datetime
from json import loads
from requests import get
from pyowm.owm import OWM


engine = speech.Speech()



def get_time():
    currentDT = datetime.datetime.now()

    engine.text_to_speech("The time is {} hours and {} minutes".format(
        currentDT.hour, currentDT.minute))

    return


from requests import get
from json import loads

def weatherForecaste(city):
    WEATHER_API_KEY = 'Your Weather_API Key'

    try:
        response = get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}")
        responseDecode = loads(response.text)
        
        if response.status_code == 200:
            weather_status = responseDecode["weather"][0]["description"]
            weather_temp = responseDecode["main"]["temp"] - 273.15
            weather_feels_like = responseDecode["main"]["feels_like"] - 273.15

            result = f"The current weather status in {city} is {weather_status}. The current temperature is {weather_temp}°C, and it feels like {weather_feels_like}°C."

            engine.text_to_speech(result)
        else:
            print(f"Error: {response.status_code} - {responseDecode['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")


city = input("Enter the city name: ")
weatherForecaste(city)



