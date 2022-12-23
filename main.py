from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class BankType(str, Enum):
    kakaobank = "카카오뱅크"
    kbank = "케이뱅크"
    toss = "토스"


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/me")
async def read_me():
    return {"user": "the current user"}


@app.get("/users/{name}")
async def read_user_name(name: str):
    return {"user": name}


@app.post("/items/")
async def read_item(item: Item):
    return {"item": item}


@app.get("/bank-types/{bank_type}")
async def get_intro(bank_type: BankType):
    if bank_type == BankType.kakaobank:
        return {"bank_type": bank_type, "msg": "같지만 다른 은행"}
    elif bank_type == BankType.kbank:
        return {"bank_type": bank_type, "msg": "모바일로 만나는 1금융권 은행"}
    elif bank_type == BankType.toss:
        return {"bank_type": bank_type, "msg": "새로운 은행을 만날 시간"}


fake_items_db = [{"name": "Ted"}, {"name": "Robin"}, {"name": "Barney"}]


@app.get("/info/")
async def read_info(skip: int = 0, limit: int = 2):
    return fake_items_db[skip : skip + limit]


@app.get("/tv-shows/{tv_show_name}")
async def read_tv_show(tv_show_name: str, character: Optional[str] = None):
    if character:
        return {"tv_show_name": tv_show_name, "character": character}
    return {"tv_show_name": tv_show_name}
