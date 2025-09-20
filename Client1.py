import requests

"""
url = "http://127.0.0.1:8000/"


data = {
    "name":"Jagan",
    "age":20
}
get_response = requests.post(url,json=data)
print(get_response.json())
"""

"""

url = "http://127.0.0.1:8000/CookieModel"

data = {
    "name":"Jagan",
    "age":20
}

get_response = requests.get(url,json=data)
print(get_response.json())
"""


"""
url = "http://127.0.0.1:8000/ResponseModel"

data = {
    "name":"Jagan",
    "age":20
}
get_response = requests.post(url,json=data)
print(get_response.json())

"""
"""
url = "http://127.0.0.1:8000/"

data = {
    "username":"Jagan",
    "password":"Jxgxn_10_@123",
    "email":"Jagan10ns@gmail.com"
}


get_response = requests.post(url,json=data)
print(get_response.json())
# if get_response.status_code!=200:
#     get_errors = get_response.json()#{[{}]}
#     print(get_errors.get('detail')[0]["msg"])
# else:
#     print(get_response.json())

"""


"""
url = "http://127.0.0.1:8000/"

data = {
    "name":"Jagan",
    "email":"jagan10ns@gmail.com",
    "password":"Jxgxn_10_@123"
}


get_response = requests.post(url,json=data)
print(get_response.json())
"""


url = "http://127.0.0.1:8000/CarModel"

data = {
    "description":"This is carmodel",
    "type":"bus"
}

get_response = requests.post(url,json=data)
print(get_response.json())