# weather.py
# Simulated external API usage

import requests


def get_temperature(city: str) -> float:
    response = requests.get(f"https://api.weather.com/{city}")
    data = response.json()
    return data["temperature"]
