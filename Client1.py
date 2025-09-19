import requests


url = "http://127.0.0.1:8000/"


data = {
    "name":"Jagan",
    "age":20
}
get_response = requests.post(url,json=data)
print(get_response.json())