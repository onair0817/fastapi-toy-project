from enum import Enum

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Optional, List


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


# @ 기본 매개변수


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

# @ 쿼리 매개변수


@app.get("/info/")
async def read_info(skip: int = 0, limit: int = 2):
    return fake_items_db[skip : skip + limit]


# @ Query 클래스 이용한 쿼리 매개변수 검증


@app.get("/tv-shows/{tv_show_name}")
# or Optional[str] = Query(None)으로 설정하면 쿼리 매개변수 값 검증 수행 e.g. 글자수 10자 이내인지
# 만일 조건을 구체화하고 싶으면 Query(None, min_length=3, max_length=10, regex="^show$")로 추가 가능
# 필수값으로 받으려면 None 대신 ...으로 대체
async def read_tv_show(tv_show_name: str, character: Optional[str] = None):
    if character:
        return {"tv_show_name": tv_show_name, "character": character}
    return {"tv_show_name": tv_show_name}


@app.get("/tv-shows/{tv_show_name}/characters")
async def read_tv_show_and_character(tv_show_name: str, character: str):
    return {"tv_show_name": tv_show_name, "character": character}


@app.get("/movies/{movie}")
async def read_user_item(movie: str, character: str):
    item = {"movie": movie, "needy": character}
    return item


@app.get("/characters/")
# Query(None) 대신 Query(['white', 'motive', 'doy']) 넣으면 빈 요청시 기본값으로 반환함
async def read_characters(q: Optional[List[str]] = Query(["white", "motive", "doy"])):
    query_items = {"q": q}
    return query_items


# @ Path 클래스 이용한 경로 매개변수 검증


@app.get("/numbers/{number_value}")
# ge: greater than or equal, lt: less than
async def read_number(
    number_value: int = Path(..., title="The value of number", ge=100)
):
    return {"number": number_value}


# @ Request Body 추가


class Drama(BaseModel):
    name: str
    description: Optional[str] = None
    score: float
    channel: Optional[str] = None


@app.put("/dramas/{drama_id}")
async def create_drama(drama_id: int, drama: Drama, q: Optional[str] = None):
    result = {"drama_id": drama_id, **drama.dict()}
    if q:
        result.update({"q": q})
    return result
