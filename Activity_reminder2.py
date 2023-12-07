import requests
from pprint import pprint  
import datetime as dt 

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}"

    # Make a request to the OpenWeatherMap API
    response = requests.get(complete_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()

        # Check if the city was found
        if weather_data["cod"] == 200:
            # Extract relevant weather information
            main_data = weather_data["main"]
            temperature = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]

            weather_description = weather_data["weather"][0]["description"]

            # Display the weather information
            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature - 273.15} C")
            print(f"Atmospheric Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Description: {weather_description}")

        else:
            print(f"City '{city_name}' not found.")

    else:
        print("Error in the request. Check your API key and try again.")
        print(f"Status Code: {response.status_code}")

api_key = "786da6a60e9ed488adc8564a55944da6"
city_name = "Philadelphia"
get_weather(api_key, city_name)

