from fastapi import FastAPI,Path,Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

@app.get("/{path}")
def main(
    path:Annotated[int,Path(gt=18,lt=55)],
    query:Annotated[int,Query(gt=18,lt=55)] = None
):
    data = {"Path():":"Path-Path Parameter","Query()":"Query-Query Parameter"}
    try:

        if query:
            data.update({"query_value":query})
        data["path_value"] = path
        return data
    except Exception as e:
        return e
    
"""
class check_path_query(BaseModel):
    path:Annotated[int,Path(gt=18,lt=55)]

@app.post("/path")
def check(get_data:check_path_query,query:Annotated[int,Query(ge=18,lt=55)]=None):
    response = get_data.dict()
    if query:
        response.update({"query":query})
    return response

"""


class check_path_query(BaseModel):
    path:Annotated[int,Path(gt=18,lt=55)] #we cam use Field() path:int = Field(default,ge=100)
    query:Annotated[int,Query(ge=18,lt=55)]=None


@app.post("/path")
def check(get_data:check_path_query):
    response = get_data.dict()
    return response


@app.get("/path/{item_id}")
def page(
    item_id:Annotated[int,Path()],
    query:str|None = Query(default=None,alias="id")
):
    print(query)
    return item_id

