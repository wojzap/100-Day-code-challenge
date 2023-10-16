import requests
from twilio.rest import Client

# Put your information below
LAT = 0
LON = 0
API_KEY = ""
OWM_Endpoint = ""
account_sid = ''
auth_token = ''

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY
}
response = requests.get(OWM_Endpoint, params=parameters)
weather_data = response.json()


# Taking information if it's going to rain in next 12 h
will_rain = True
for hour in range(0, 12):
    if weather_data["hourly"][hour]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.",
        from_="+18316235899",
        to="+48793480033"
    )
    print(message.status)