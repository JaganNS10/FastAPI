from fastapi import FastAPI,HTTPException,status,Request
from fastapi.responses import JSONResponse,PlainTextResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()


items = {"foo":"Hello world","boo":"welcome to fastapi"}
@app.get("/item/{item_id}",tags=["swagger documentation purpose"])
def status_404(item_id:str):
    if item_id not in items:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"X-error":"Your errors"}
        )
    return {"item":items[item_id]}



#CustomException

class UnicornException(Exception):
    def __init__(self,name:str): #First
        self.name=name
        print("Hello")


@app.exception_handler(UnicornException)#Second
def Unicorn_Exception(request:Request,exc:UnicornException):
    print("coming in Unicorn_Exception")
    print("request:",request.url)
    print("exc:",exc.name)
    return JSONResponse(
        status_code=status.HTTP_402_PAYMENT_REQUIRED,
        content={"msg":f"check your {exc.name}"}
    )


@app.get("/exception/{name}")
def CustomException(name:str):
    if name.isnumeric():
        raise UnicornException(name=name)
    return {"name":name}




#RequestValidationError -> if the path or query or missing required field this will trigger.

@app.exception_handler(RequestValidationError)
def invalid_exception(request,exc):
    print("coming in requestvalidatorerror")
    print(request)
    print(exc)
    return PlainTextResponse(str(exc),status_code=400)


@app.get("/requestvalidation/{name}")
def requestvalidationerror(name:int):
    return name