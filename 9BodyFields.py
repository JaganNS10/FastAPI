from fastapi import FastAPI,Query,Body,Path
from typing import Annotated,List,Union
from pydantic import BaseModel,Field,HttpUrl
from decimal import Decimal

app = FastAPI()


class Filter(BaseModel):
    model_config = {"extra":"forbid"}
    name:str = Field(description="name of the person",max_length=300)
    age:int = Field(gt=18) 
    description:str  =  Field(default=None)

@app.post("/path/{item_id}")
def main(item_id:int,item:Annotated[Filter,Body(embed=True)]):
    return item

#url = f"http://127.0.0.1:8000/path/{1}/?name=Jagan"
#item_id:int,item:Annotated[Filter,Query()] IN POST
#"POST /path/1?name=Jagan HTTP/1.1" 200

"""
class check(BaseModel):
    name:str
    description:str|None = None
    age:int
    price:float
    tags:list = []


#IN THIS the list cannot say what type elements it will store . so use List from typing

@app.post("/")
def page1(item:check):
    return item
"""

class check(BaseModel):
    name:str
    age:int = Field(gt=17)
    description:Union[str,None] = None
    acc:int = Field(ge=0)
    tags:List[str] = []


@app.post("/")
def page1(item:check):
    return item



#Nested Models

class Image(BaseModel):
    name:str
    # url:str 
    url:HttpUrl #from pydantic import Httpurl

class NestedModel(BaseModel):
    name:str = Field(max_length=300)
    age:int = Field(gt=18)
    #image:Image|None = None #{"name":"1.jpg","url":"http//google.com"}
    image:List[Image] = None #[{"name":"","url":""},{"name":"","url":""}]



@app.post("/nestedmodel/")
def Model(item:NestedModel):
    return item



#Deeply Nested Models
class Offer(BaseModel):
    items:List[NestedModel|None] = None


@app.post("/deeplynestedmodel/")
def DeeplyNestedModel(items:Offer):
    return items



