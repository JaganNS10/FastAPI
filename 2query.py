from fastapi import FastAPI


app = FastAPI()


db = [
    {"page1":"Hello"},
    {"page2":"world"},
    {"page3":"welcome"},
    {"page3":"to"},
    {"page4":"python"}
]

print(db[0:10])

@app.get("/items")
def main(skip:int=0,limit:int=10):#http://localhost:8000/items/?skip=2&limit=8
    print(skip)
    print(limit)
    return db[skip:skip+limit]



@app.get("/path1/{item}")#http://localhost:8000/path1/10?q=jagan
def page1(item:int,q:str | None = None): #| union type operator q value is either str or None
    print(q)
    print(item)
    if q:
        return {"item":item,"q":q}
    return {"item":item,"q":q}



@app.get("/path2/{item}")

def page2(item:int,q:str | None = None , short:bool = False):
    D = {"item":item}
    print(q)
    if q:
        D['q'] = q
    if not short:
        D.update({"message":"short is True"})

    return D


@app.get("/items/{user_id}/path/{item_id}")
def page3(user_id,item_id,q:str|None=None):
    return {"user_id":user_id,"item_id":item_id,"q":q}



#Note if you are using query paramater set the default value.