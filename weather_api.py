import requests
city = input("Enter city: ")
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()
current = data["current_condition"][0]
print("\nWeather Details")
print("----------------")
print("City:", city)
print("Temperature:", current["temp_C"], "°C")
print("Feels Like:", current["FeelsLikeC"], "°C")
print("Humidity:", current["humidity"], "%")
print("Weather:", current["weatherDesc"][0]["value"])
search = input("\nSearch temperature/humidity/weather: ").lower()
if search == "temperature":
    print("Temperature:", current["temp_C"], "°C")
elif search == "humidity":
    print("Humidity:", current["humidity"], "%")
elif search == "weather":
    print("Weather:", current["weatherDesc"][0]["value"])
else:
    print("No matching result found.")