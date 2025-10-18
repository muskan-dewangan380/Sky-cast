# ------------------- GUI SETUP -------------------
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