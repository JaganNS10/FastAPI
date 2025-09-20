import requests


url = "http://127.0.0.1:8000/FormModel"

data = {
    "username":"Jagan",
    "password":"Jxgxn_10_2005",
    "age":20
}

get_response = requests.post(url,data=data)
print(get_response.json())