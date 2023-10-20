import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
query = input("Tell me which exercises you did: ")
exercise_config = {
    "query": query,
    "gender": "male",
    "weight_kg": 85,
    "height_cm": 175,
    "age": 27
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
exercise_data = response.json()
print(response.text)

sheety_endpoint = "https://api.sheety.co/d3889b37b31752549849bbc26d475eb1/myWorkouts/workouts"

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for exercise in exercise_data["exercises"]:
    exercise_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    sheety_config = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=sheety_endpoint, json=sheety_config, headers=exercise_headers)
    print(response.text)


