# use twilio to send sms now!!!!
import requests
from appier import message

#from twilio.rest import Client

#account_sid = ""
#auth_token = ""
# client = Client(account_sid, Auth token)
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_Key = "fcf52811a357cb45314bbe979f050b1d"

weather_params = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": API_Key,
}

response = requests.get(ENDPOINT, params=weather_params)
response.raise_for_status()
forecast_data = response.json()["list"][:12]
will_rain = False
for hour_data in forecast_data:
    slice_data = hour_data["weather"][0]["id"]
    print(slice_data)
    if slice_data < 600:
        will_rain = True
        break
# if will_rain:
    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #    .create(
    #    body="Bring your umbrella",
#        from=''   -> your number,
    #    to = ''   -> your number)
    #      print(message.status)

# go to python anywhere and set it up online so that you won't have to run it each time... simple!!!
