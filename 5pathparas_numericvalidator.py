from fastapi import FastAPI,Query,Path
from typing import Annotated

app = FastAPI()


@app.get("/{item}")
def main(item:Annotated[int,Path(title='path parameters and numeric validators')],
         q:Annotated[str,Query(title="Hii",description="hello world",alias="name")]=None
        ):
    data = {"message":"Hello world"}
    print(item)
    if q:
        data['q'] = q
    return data




#ge,le -> greater than or equal to and less than or equal to 
#gt,lt -> greater than and less than


@app.get("/path/{Number}")
def page1(
    Number:Annotated[int,Path(title="gt",gt=18,lt=55)]
):
    data = {"message":"Hello world"}
    data["Number"] = Number
    
    return data

    

#String validator -> Query() -> Query validator
#Number validator -> Path() -> path validator



