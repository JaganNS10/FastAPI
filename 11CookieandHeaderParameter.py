from fastapi import FastAPI,Cookie,Header,Body
from typing import Annotated
from pydantic import BaseModel,Field
import requests


app = FastAPI()


@app.get("/CookiePage")
def cookie(id:Annotated[str,Cookie()]=None):
    print(id)
    return {"message":"hello world","id":id}


@app.get("/Headerpage")
def header(first_name:Annotated[str,Header(convert_underscores=False)]=None):
    print(first_name)
    return {"first_name":first_name}

#Header(convert_underscores=False) if i give parameter like this first_name it will display 
#like first-name.so use convert_underscores=False to make this same as parameter.

"""
url = "http://127.0.0.1:8000/CookiePage"
get_response = requests.get(url,cookies={"id":"Jagan"})
print(get_response.json())


url = "http://127.0.0.1:8000/Headerpage"

get_response = requests.get(url,headers={"first_name":"Jagan"})
print(get_response.json())
print(get_response.headers)
"""

"""
class CookieModel(BaseModel):
    name:str=None
    age:int=None
    description:str = None

@app.post("/CookieModel")
def CookieFun(item:Annotated[CookieModel,Cookie()]):
    return item
"""

class CookieModel(BaseModel):
    name:str
    age:int
    description:str = None


@app.get("/CookieModel")
def CookieFun(item:Annotated[CookieModel,Cookie()]):
    return item

class HeaderModel(BaseModel):
    name:str
    age:int = None
    description:str = None


@app.get("/HeaderModel")
def HeaderFun(item:Annotated[HeaderModel,Header()]):
    return item