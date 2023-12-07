import requests
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
#import threading
#import pygame
#import os 

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
            temperature = ((main_data["temp"] - 273.15)*9/5)+32  # Convert temperature to Celsius
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

#def play_audio():
    #pygame.mixer.init()
    #pygame.mixer.music.load("bird.mp3")  
    #pygame.mixer.music.play()

def close_window():
    #pygame.mixer.music.stop()
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

    image_cold_path = "/Users/camilajin/Desktop/Project 2/cold.png"
    image_hot_path = "/Users/camilajin/Desktop/Project 2/hot.png"
    if temperature < 77: # 25C
        imgcold = Image.open(image_cold_path)
        imgcold = imgcold.resize((100,100), Image.ANTIALIAS)
        tk_imgcold = ImageTk.PhotoImage(imgcold)
        image_cold_label = tk.Label(root, image=tk_imgcold)
        image_cold_label.pack()
    else:
        imghot = Image.open(image_hot_path)
        imghot = imghot.resize((100,100), Image.ANTIALIAS)
        tk_imghot = ImageTk.PhotoImage(imghot)
        image_hot_label = tk.Label(root, image=tk_imghot)
        image_hot_label.pack()

    message_label = tk.Label(
        root,
        text=(
            "Hi, Mr. Li, It's time to move!\n"
            f"李先生，动起来！\n \n"
            f"Today's weather in Philadelphia:\n"
            f"费城今天的气候是：\n \n"
            f"Temperature/温度: {temperature:.2f} F\n"
            f"Humidity/湿度: {humidity}%\n"
            f"Description/气候形容: {weather_description}"
        ),
        font=("Helvetica",25)
    )
    message_label.pack(pady=20)

    # Button to close the window and stop audio
    close_button = tk.Button(root, text="OK", command=close_window, font=("Helvetica", 18))
    close_button.pack(pady=10)

    # Pop-up Window size
    root.geometry("800x500")

    # Audio playing
    #audio_thread = threading.Thread(target=play_audio)
    #audio_thread.start()

    root.mainloop()