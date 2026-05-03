import requests
import os
print("Weather App")
city = input("Enter city name: ").strip()
# simple check
if city == "":
    print("Please enter a city name")
else:
    api_key = os.getenv("WEATHER_API_KEY")
    if api_key is None:
        print("API key not found. Please set it using setx.")
    else:
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                condition = data["weather"][0]["description"]
                print("\n--- Weather Report ---")
                print("City:", city)
                print("Temperature:", round(temp, 1), "°C")
                print("Humidity:", humidity, "%")
                print("Condition:", condition.title())
            else:
                print("Error:", response.json().get("message", "Unknown error"))
        except:
            print("Network error. Please check your internet connection.")
