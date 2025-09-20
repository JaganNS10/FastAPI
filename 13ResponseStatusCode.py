from fastapi import FastAPI,Query
from pydantic import BaseModel,Field,EmailStr
from typing import Annotated

app = FastAPI()



class UserIn(BaseModel):
    username:str = Field(max_length=200)
    password:str
    email:EmailStr



class UserInDb(BaseModel):
    username:str
    hashed_password:str
    email:EmailStr


def get_user(getuser:UserIn):#def get_user(getuser):
    get_password = "supersecretpassword"+getuser.password
    get_db_details = UserInDb(**getuser.dict(),hashed_password=get_password)
    print(get_db_details)
    return get_db_details

@app.post("/")
def CreateUser(request:UserIn):
    send = get_user(request)
    return send





# def aribitery_keyword_argument(**kwargs):
#     def get_name(name,**kwargs):
#         print(name)
#         print(kwargs)

#         def get_age(age,**kwargs):
#             print(age)
#             print(kwargs)

#             def get_salary(salary,**kwargs):
#                 print(salary)
#                 print(kwargs)

#             get_salary(**kwargs)
#         get_age(**kwargs)
#     get_name(**kwargs)

# aribitery_keyword_argument(name="Jagan",age=20,salary=20000)


# class One():
#     def __init__(self,name,salary):
#         self.Name = name
#         self.salary = salary


# class Two(One):
#     def __init__(self,age,**kwargs):
#         self.age = age
#         super().__init__(**kwargs)

# Object = Two(name='Jagan',age=20,salary=20000)

# print(Object.age)
# print(Object.Name)
# print(Object.salary)