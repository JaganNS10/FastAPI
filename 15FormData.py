from fastapi import FastAPI,Form
from typing import Annotated

app = FastAPI()

#see Client2.py and SendData.html use data="" instead json = "" while using import requests page.
@app.post("/",response_model=dict[str,str])
def get_details(username:Annotated[str,Form()],password:Annotated[str,Form()]):
    print(True)
    return {"username":username}