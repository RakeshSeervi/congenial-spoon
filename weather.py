from datetime import datetime
import os
import pytz
import requests
import math

API_KEY = 'e64142d5d03e96f67de1b9372b0ee4cf'

API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

def query_api(city):    
    try:        
        print(API_URL.format(city, API_KEY))        
        data = requests.get(API_URL.format(city, API_KEY)).json()    
    except Exception as exc:        
        print(exc)        
        data = None    
    
    return data
