from fastapi import FastAPI,Query
from typing import Annotated,Literal
from pydantic import BaseModel,Field

app = FastAPI()


class Filter(BaseModel):
    model_config = {"extra":"forbid"}
    limit:int = Field(default=100,gt=0,le=100)
    offset:int = Field(default=0,ge=0)
    order_by:Literal['created','updated'] = 'created'
    tags:list[str] = []


#path:Annotated[int,Path(gt=18,lt=55)] #we can use Field() path:int = Field(default,ge=100)

#QueryParameter see this clearly
@app.get("/")
def main(get_filters:Annotated[Filter,Query()]):
    print(get_filters)
    return get_filters

"""So yes — you’re absolutely right: if the Pydantic model has defaults via Field(...), and 
you write item: Annotated[Model, Query()], FastAPI will honor those defaults without needing to 
put them in Query() again.

#shows error but in Field() we are not default value.

# class check(BaseModel):
#     age:int = Field()
# @app.get("/")
# def main(item:Annotated[check,Query()]):
#     return item

""" 

#model_config = {"extra_fields":"forbid"}

#In this url extra field id is included.-> id=1

#http://localhost:8000/?limit=4&offset=10&order_by=updated&tags=[%22Jagan%22]&id=1

"""
@app.get("/")

def main(
    limit:int = Query(default=100,gt=0,lt=101),
    offset:int = Query(default=0,ge=0),
    order_by:Literal["created","updated"] = "created",
    tags:list[str] = []
):
    data = {
        "limit":limit,
        "offset":offset,
        "order_by":order_by,
        "tags":tags
    }

    return data
"""



"""

class Filter(BaseModel):
    model_config = {"extra": "forbid"}
    limit: int = Field(default=100, gt=0, le=100)
    offset: int = Field(default=0, ge=0)
    order_by: Literal['created', 'updated'] = 'created'
    tags: list[str] = []

@app.post("/")
def main(get_filters: Filter):
    print(get_filters)
    return get_filters
"""