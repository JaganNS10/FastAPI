from fastapi import FastAPI,status
from pydantic import BaseModel,EmailStr

app = FastAPI()


class UserBase(BaseModel):
    name:str
    email:EmailStr


#To access this Model . we need name and email.because it inherit UserBase Model
class UserIn(UserBase): 
    password:str           


#To access this Model . we need name and email.because it inherit UserBase Model
class UserDb(UserBase):
    hashed_password:str


"""
@app.post("/")
def User(request:UserIn):
    return request
"""

def access_db(getUserIn):
    create_hassed_password = "supersecret"+getUserIn.password
    get_hashed_password = UserDb(**getUserIn.dict(),hashed_password=create_hassed_password)
    return get_hashed_password

@app.post("/")
def User(request:UserIn):
    get_data = access_db(getUserIn=request)
    return get_data



class BaseModel1(BaseModel):
    description:str
    type:str


class CarModel(BaseModel1):
    type:str = "Car"

class PlaneModel(BaseModel1):
    type:str = "Plane"



@app.post("/CarModel",response_model=CarModel|PlaneModel)
def User(request:BaseModel1):
    if request.type == "Car":
        return CarModel(**request.dict())
    elif request.type == "Plane":
        return PlaneModel(**request.dict())



#response_model -> Our api response should match what you are given in the response_model=""

@app.get("/response",response_model=dict[str,float])
def Response_Model():
    # return {"foo":3.12,"price":900.98,"list":[]}
    # return []
    return {"foo":3.12,"price":900.98}


@app.get("/responsemodel",response_model=CarModel,status_code=status.HTTP_200_OK)
def Response_BaseModel():
    return {"description":"This is car model","type":"Plane"}


