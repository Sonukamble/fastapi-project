from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Data(BaseModel):
    name:str
    age:int

@app.get("/")
def read_root():
    return {"Hello":"world"}

@app.get("/items/{item_id}")
def read_item(item_id: int,q: Union[str,None]=None):
    return {"item_id":item_id,"q":q}

@app.post("/items")
def pst_item(data: Data):
    return(data.name,data.age)