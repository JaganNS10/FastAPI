from fastapi import FastAPI,Body
from typing import Annotated
from pydantic import BaseModel


app = FastAPI()


class check_types(BaseModel):
    name:str #required
    description:str|None = None #not required
    age:int #required



class user(BaseModel):
    salary:int
    address:str = None

# @app.get("/")
# def main(item:check_types):#required one 
#     pass

@app.get("/")
def main(item:check_types=None):
    return item

@app.post("/page1")
def two_meta_classes(item:check_types=None,user:user=None):
    data = {
        "item":item,
        "user":user
    }
    return data



#directly passed in function without using BaseModel


@app.post("/page2")
def using_body(important:Annotated[int ,Body()]):
    return important


"""
def add(*,a,b):
    return a+b

print(add(1,2))#wrong
print(add(a=1,b=2)) using * . we have to use keyword arguments not positional arguments.
"""

#error -> positional arguments follows keyword argument: answer use * 
#def using_multiple_body(user:user=None,important:Annotated[int ,Body()]):


@app.post("/page3")
def using_multiple_body(*,user:user=None,important:Annotated[int ,Body()]):
    data = {
        "user":user,
        "important":important
    }

    return data

#embed=True means you can pass data like this {"important":10} instead json=10
@app.post("/page4")
def using_embed(important:Annotated[int,Body(embed=True)]):
    print(important)
    return important

"""
@app.post("/page5")
def using_embed_basemodel(important:check_types):
    return important
"""

#Both are same 

@app.post("/page5")
def using_embed_basemodel(important:Annotated[check_types,Body(embed=True)]):
    return important


@app.post("/page6")
def using_multiple_body(*,a:Annotated[int,Body()],b:Annotated[int,Body()]):
    return a,b
