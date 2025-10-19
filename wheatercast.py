#weather_app_gui_india.py

import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    api_key = "88dcc494b09f1373a3781f237d4d412a"  
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": f"{city},IN",
        "appid": api_key,
        "units": "metric",
        "lang": "en"
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()

            city_name = data['name']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']
            condition = data['weather'][0]['description'].capitalize()
            sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime("%I:%M %p")
            sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime("%I:%M %p")

            result_label.config(
                text=(
                    f" {city_name}, IN\n"
                    f" Temperature: {temp}°C (Feels like {feels_like}°C)\n"
                    f" Condition: {condition}\n"
                    f" Humidity: {humidity}% | 🧭 Pressure: {pressure} hPa\n"
                    f" Wind: {wind} m/s\n"
                    f" Sunrise: {sunrise} | 🌇 Sunset: {sunset}"
                ),
                fg="#003366"
            )

        elif response.status_code == 404:
            messagebox.showerror("Error", "City not found. Try another city.")
        else:
            messagebox.showerror("Error", f"Failed to fetch data. (Code: {response.status_code})")

    except Exception as e:
        messagebox.showerror("Connection Error", f"Something went wrong:\n{e}")
#GUI SETUP
root = tk.Tk()
root.title("🌦 Smart Weather App - India")
root.geometry("500x400")
root.config(bg="#E8F0FE")

title_label = tk.Label(root, text="🇮🇳 Smart Weather App", font=("Arial", 20, "bold"), bg="#E8F0FE", fg="#1A237E")
title_label.pack(pady=15)

city_frame = tk.Frame(root, bg="#E8F0FE")
city_frame.pack(pady=10)

city_label = tk.Label(city_frame, text="Enter City:", font=("Arial", 12), bg="#E8F0FE")
city_label.pack(side="left", padx=5)

city_entry = tk.Entry(city_frame, font=("Arial", 12), width=25, bd=2, relief="groove")
city_entry.pack(side="left", padx=5)

get_btn = tk.Button(root, text="Get Weather ☁", font=("Arial", 12, "bold"), bg="#3949AB", fg="white", command=get_weather)
get_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), bg="#E8F0FE", justify="left", wraplength=450)
result_label.pack(pady=20)

footer_label = tk.Label(root, text="Developed by Master 👑 | Data from OpenWeatherMap", font=("Arial", 9), bg="#E8F0FE", fg="#555")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
