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



@app.get("/path/{item_id}")
def page(
    item_id:Annotated[int,Path()],
    query:str|None = Query(default=None,alias="id")
):
    print(query)
    return item_id

