from fastapi import FastAPI


app = FastAPI()

print(app)

@app.get("/")
def main():
    return {"message":"Hello world"}


@app.get("/page1/{pathparas}")
def get_paras(pathparas):
    return {"pathparamter":pathparas}


@app.get("/page2/{pathparas}")
def get_intparas(pathparas:int): #the path must be same that is passed inside the fun.
    return {"parasint":pathparas}


# @app.get("/page3/me")
# def hello():
#     return [1,2]

@app.get("/page3/me")
def get_path_me():
    return {"user_id":"the current user"}



from enum import Enum

class ModelName(str,Enum):
    name1 = "Jagan"
    name2 = "Hemanth27"
    name3 = "Jothi"

Object = list(ModelName)


"""
ModelName looks like 
{
    "name1":ModelName("Jagan"),
    "name2":ModelName("Hemanth27"),
    "name3":ModelName("Jothi")
}
"""
print(ModelName.name1)
print(ModelName.name1.value=="Jagan")
print(ModelName.name1.value)
print(ModelName.name1.upper())


@app.get("/enum/{model_name}")
def enumfun(model_name:ModelName):
    print('model_name:',model_name) #ModelName.name1 or ModelName.name2...
    print("ModelName.Name1:",ModelName.name1)
    if model_name is ModelName.name1: 
        return {"model_name":model_name,"ModelName.name1":ModelName.name1}
    #model_name.value  model_name = Jagan
    if model_name.value == "Hemanth27": 
        return {"model_value":model_name}