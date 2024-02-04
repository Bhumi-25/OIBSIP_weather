
from dotenv import load_dotenv
import os
load_dotenv()

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Make sure to install the Pillow library
import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        display_weather(weather_data)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")

def display_weather(weather_data):
    result_text.set(f"City: {weather_data['name']}\n"
                    f"Temperature: {weather_data['main']['temp']}°C\n"
                    f"Humidity: {weather_data['main']['humidity']}%\n"
                    f"Weather Condition: {weather_data['weather'][0]['description']}\n"
                    f"Rain: {weather_data.get('rain', {}).get('1h', 0)} mm\n"
                    f"Wind Speed: {weather_data['wind']['speed']} m/s\n"
                    f"Visibility: {weather_data.get('visibility', 'N/A')} meters")

def on_submit():
    location = location_entry.get()
    get_weather(api_key, location)

api_key = os.getenv("WEATHER_API_KEY")
  # Replace with your OpenWeatherMap API key

app = tk.Tk()
app.title("Weather App")
app.geometry("400x400")  # Adjust dimensions as needed

# Load and display the weather background image
weather_image = Image.open("weater.jpg")  # Replace with the actual file path
weather_image = ImageTk.PhotoImage(weather_image)
background_label = tk.Label(app, image=weather_image)
background_label.place(relwidth=1, relheight=1)

# Header
header_label = tk.Label(app, text="Weather App", font=("Arial", 20, "bold"), fg="black")
header_label.pack(pady=10)

# Location Entry
location_label = tk.Label(app, text="Enter city or ZIP code:", font=("Arial", 12, "bold"), fg="black")
location_label.pack(pady=5)

location_entry = tk.Entry(app, font=("Arial", 12, "bold"))
location_entry.pack(pady=10)

# Submit Button
submit_button = tk.Button(app, text="Get Weather", command=on_submit, font=("Arial", 12, "bold"))
submit_button.pack(pady=15)

# Result Display
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, font=("Arial", 12, "bold"), fg="black", justify="left")
result_label.pack()

app.mainloop()
