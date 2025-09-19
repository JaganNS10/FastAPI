from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Filter(BaseModel):
    name:str = Field(examples=['Your name'])
    age:int

    model_config = {
        "json_schema_extra":{
        "example":[
            {
                "name":"your name",
                "age":"your age"
            }
        ]
    }
}


@app.post("/")
def json_schema(para:Filter):
    return para