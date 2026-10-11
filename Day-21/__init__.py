import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "dangi"
token = "zxcs67okjh"
pixela_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(pixela_endpoint, json=pixela_params)
# print(response.text)

# username created!!! We do not have to use the request post in future

# graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"

headers = {
    "X-USER-TOKEN": token
}
Graph_ID = "cycling"
graph_config = {
    "id": Graph_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.date(year=2026, month=10, day=10)
print(today.strftime("%Y%m%d"))

pixel_config = {
    "quantity": "20"
}

pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{Graph_ID}/{today.strftime('%Y%m%d')}"
pixel = requests.put(pixel_endpoint, json=pixel_config, headers=headers)
print(pixel.text)

update_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{Graph_ID}/{today.strftime('%Y%m%d')}"
updated_config = {
    "quantity": "15"
}
updates = requests.put(update_endpoint, json=updated_config, headers=headers)
print(updates.text)


# use delete in same manner!!!!!