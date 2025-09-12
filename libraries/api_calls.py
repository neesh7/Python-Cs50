import requests
import json


# Coordinates for a location (e.g., Bangalore)
latitude = 12.97
longitude = 77.59

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response = requests.get(url)
# print(response.json())
print(json.dumps(response.json(), indent=2))
print(json.dumps(response).json())
# if response.status_code == 200:
#     data = response.json()
#     weather = data['current_weather']
#     print(f"Temperature: {weather['temperature']}°C")
#     print(f"Windspeed: {weather['windspeed']} km/h")
#     print(f"Weather Code: {weather['weathercode']}")
# else:
#     print("Could not retrieve weather data.")

