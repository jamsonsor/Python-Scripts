import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.environ.get("WEATHER_API_KEY")
api_url = "https://api.openweathermap.org/data/2.5/weather"

while True:
  city = input("Write your city:")

  if city.lower() == 'q':
    break   # Exit the loop if the user enters 'q'

  response = requests.get(
    url=api_url,
    params={
      "q": city,
      "appid": api_key,
      "units": "metric",
    }
  )

  if response.status_code == 200:
    weather_data = response.json()
    print(city, "temperature is", weather_data['main']['temp'], "degrees celcius.")
  elif response.status_code == 401:
    print("Invalid API key detected, exiting the script.")
    break
  else:
    print("City not found. Please check the spelling and try again.")