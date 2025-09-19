import requests

"""
url =  "http://127.0.0.1:8000/page1/"
data = {
    "name":"Jagan",
    "age":20,
    "price":899.0
}
get_response = requests.post(url,json=data)
print(get_response.json())
"""

"""
url =  f"http://127.0.0.1:8000/page2/{1}"

get_response = requests.post(url)
print(get_response.json())
"""

"""
url =  f"http://127.0.0.1:8000/page3/"

get_response = requests.post(url,json={"cusid":2})
print(get_response.json())
"""

"""

url =  f"http://127.0.0.1:8000/page4/{3}/?q=jagan"
url =  f"http://127.0.0.1:8000/page4/{3}"

get_response = requests.post(url,json=data)
print(get_response.json())
"""



"""
url = f"http://127.0.0.1:8000/path"

# data = {
#     "path":19,
#     "query":20
# }

data = {
    "path":19
}



get_response_from_api = requests.post(url,json=data)
print(get_response_from_api.json())
"""

"""
url = "http://127.0.0.1:8000/"

data = {
    "name":"Jagan",
    "age":20
}

get_response = requests.get(url,json=data)
print(get_response.json())
"""


"""
url = "http://127.0.0.1:8000/page1"

data = {
    "item":{"name":"Jagan","age":20},
    "user":{"salary":20000}
}
get_response = requests.post(url,json=data)

print(get_response.json())
"""

"""
url = "http://127.0.0.1:8000/page2"


get_response = requests.post(url,json=10)

print(get_response.json())
"""


"""
url = "http://127.0.0.1:8000/page3"

data = {
    "user":{"salary":20000,"address":"No 297 rajaji street tv puram"},
    "important":20
}

get_response = requests.post(url,json=data)
print(get_response.json())
"""

"""
#using Body(embed=True)
url = "http://127.0.0.1:8000/page4"

data = {
    "important":10
}

get_response = requests.post(url,json=data)
print(get_response.json())
"""

"""
url = "http://127.0.0.1:8000/page5"

data = {
    "important":{
    "name":"Jagan",
    "age":20
    }
}

get_response = requests.post(url,json=data)
print(get_response.json())
"""


url = "http://127.0.0.1:8000/page6"

data = {
    "a":10,
    "b":20
}
get_response = requests.post(url,json=data)
print(get_response.json())