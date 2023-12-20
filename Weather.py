# Interacting with API in python

import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
base_URL = os.getenv("BASE_URL")

# queries with the base url
city = input("enter the city name: ")

request_url = f"{base_URL}?appid={api_key}&q={city}"

# Now making a API request
response = requests.get(request_url)

# Checking for success of the request
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temp = int(data['main']['temp']-273.15)
    print(temp)
else:
    print("An error occurred while fetching you data")
