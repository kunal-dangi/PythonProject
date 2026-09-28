import requests as rq
import datetime as dt
# response = rq.get(url="https://api.kanye.rest/", timeout=10)
# response.raise_for_status()
# data = response.json()
# quote = data["quote"]
# print(quote)

parameters = {
    "lat": 18.520430,
    "lng": 73.856743,
    "formatted": 0
}

rp = rq.get(url="https://api.sunrise-sunset.org/json", params=parameters, timeout=10)
rp.raise_for_status()
data = rp.json()
Sunrise = data["results"]["sunrise"]
Sunset = data["results"]["sunset"]
current_time = dt.datetime.now()
sunset_lst = Sunset.split("T")
sunrise_lst = Sunrise.split("T")

print(sunset_lst[1].split(":"), sunrise_lst[1].split(":"))

