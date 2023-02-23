from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: str
#     full_name: Optional[str] = None


# class UserOut(BaseModel):
#     username: str
#     email: str
#     full_name: Optional[str] = None


# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str
#     email: str
#     full_name: Optional[str] = None


class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items/", response_model=List[Item])
async def read_items():
    return items
