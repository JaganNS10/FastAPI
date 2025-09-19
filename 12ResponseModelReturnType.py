from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Filter(BaseModel):
    name:str
    age:int


@app.post("/ResponseModel")
def ResponseModel(item:Filter) -> Filter:
    return item


@app.get("/")
def ReturnType() -> list[Filter]:
    return [
        Filter(name="Jagan",age=20),
        Filter(name="Hemanth",age=24)
    ]