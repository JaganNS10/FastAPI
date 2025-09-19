from fastapi import FastAPI
from pydantic import BaseModel

# A request body is data sent by the client to your API. 
# A response body is the data your API sends to the client.


#json -> BaseModel
#pathparameter -> normal function

class check_types(BaseModel):
    name:str
    age:int
    description:str|None=None
    price:float
    tax:float|None=None


app = FastAPI()

@app.post("/page1/")
def main(item:check_types):
    change_into_dict = item.dict()
    print(change_into_dict)
    return change_into_dict



names = {
    1:{"name":"Jagan","age":20,"accno":2908128932},
    2:{"name":"hemanth","age":24,"accno":9089767}
}

@app.post("/page2/{item_id}")
def requestbody_pathparas(item_id):
    print(type(item_id))
    if int(item_id) in names:
        return names[int(item_id)]
    else:
        return {"message":"customer id not found"}
    

class check_item(BaseModel):
    cusid:int


@app.post("/page3/")
def request_path(item:check_item):
    data = item.dict()
    print(type(item.cusid))#{'cusid': 1}
    if data.get("cusid") in names:
        return names[data.get("cusid")]
    else:
        return {"message":"customerid not found"}




#item -> name='Jagan' age=20 description=None price=899.0 tax=None **item
@app.post("/page4/{item_id}")
def request_pathparas_queryparas(item_id:int,item:check_types,q:str|None = None):
    change_into_dict = item.dict()
    print(item)
    data = {"item_id":item_id,"details":change_into_dict}
    if q:
        data.update({"q":q})
    return data
