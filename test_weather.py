import requests
import tkinter as tk
import threading
import pygame

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
            temperature = main_data["temp"] - 273.15  # Convert temperature to Celsius
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            weather_description = weather_data["weather"][0]["description"]

            return temperature, pressure, humidity, weather_description

        else:
            print(f"City '{city_name}' not found.")
            return None

    else:
        print("Error in the request. Check your API key and try again.")
        print(f"Status Code: {response.status_code}")
        return None

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("bird.mp3")  
    pygame.mixer.music.play()

def close_window():
    pygame.mixer.music.stop()
    root.destroy()

# API key and city name
api_key = "652aeb37112f631f46e61c94bdf0ee1f"
city_name = "Philadelphia"

# Get weather information
weather_info = get_weather(api_key, city_name)

if weather_info:
    temperature, pressure, humidity, weather_description = weather_info

    # Tkinter window
    root = tk.Tk()
    root.title("Activity Reminder")

    message_label = tk.Label(
        root,
        text=(
            "Hi, Mr. Li! It's time to move!\n"
            f"This is today's weather in Philadelphia:\n"
            f"Temperature: {temperature:.2f} C\n"
            f"Atmospheric Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Description: {weather_description}"
        ),
        font=("Helvetica", 20)
    )
    message_label.pack(pady=20)

    # Button to close the window and stop audio
    close_button = tk.Button(root, text="OK", command=close_window, font=("Helvetica", 18))
    close_button.pack(pady=10)

    # Pop-up Window size
    root.geometry("800x300")

    # Audio playing
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()

    root.mainloop()