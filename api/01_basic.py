from enum import Enum
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


#


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
        # return {"item_id": item_id, "q": q}
    if not short:
        item.update({"desc": "description"})
    return item


#


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


#


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "DL FTW"}
    elif model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "LeCNN"}
    else:
        return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


#


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# @app.post("/item_create/")
# async def create_item(item: Item) -> Item:
#     return item


@app.put("/item_create/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None) -> dict:
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
