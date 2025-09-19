from fastapi import FastAPI,Query
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()

@app.get("/")
def main(q:Annotated[str|None,Query(max_length=10)]=None):
    result = {"message":[{1:"One",2:"Two"}]}
    if q:
        result.update({"q":q})
    return result

"""
@app.get("/page1")
def page1(q:Annotated[str | None,Query()] = None):
    print(q)
    return {"message":"Helo world"}
"""
# both are same 
"""
@app.get("/page1")
def page1(q:str|None  = Query(default=None,max_length=10)):
    print(q)
    return {"message":"Helo world"}

"""
"""
@app.get("/page1")
def page1(q:Annotated[str|None,Query(min_length=3,max_length=10)]=None):
    print(q)
    return {"message":"Helo world"}

"""


@app.get("/page1")
def page1(q:str|None=Query(default=None,min_length=2,max_length=10,pattern="^Jagan$")):
    print(q)
    return {"message":"Helo world"}



#^ no characters before the text  ^Jagan$ (N.S Jagan)->wrong
#$ no character after the text ^Jagan$ (Jagan N.S)-> wrong


#Note it is required field .without using default value like str|None = None
"""
@app.get("/page2")
def page2(q:str|None):
    print(q)
    return {"message":"Hiii"}
"""
@app.get("/page2")
def page2(q:Annotated[str,Query(title='Hello',description='hii',deprecated=True)]="QueryPara"):
    print(q)
    return {"message":"Hiii"}









