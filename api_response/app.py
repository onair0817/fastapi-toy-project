from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


# @ path operation에 response model 타입 선언하는 case
# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     return item


# @ 모델 변수에 기본값 설정할 수 있음
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


# # @ 동일한 모델로 입출력을 구성하면 문제가 되는 case (password 정보 유출)
# # Don't do this in production!
# @app.post("/user/", response_model=UserIn)
# async def create_user(user: UserIn):
#     return user


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


# @ 기본값은 응답에 포함되지 않고 설정된 값만 포함시킴
# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# @ 응답 모델에 포함시킬 요소와 제외할 요소를 설정할 수 있음
@app.get(
    "/items/{item_id}",
    response_model=Item,
    response_model_exclude_unset=True,
    response_model_include=["name", "description"],
    response_model_exclude=["tax"],
)
async def read_item(item_id: str):
    return items[item_id]
