from fastapi import Depends, FastAPI

# dependencies 모듈 import
from .dependencies import get_query_token, get_token_header
from .internal import admin

# router 서브모듈 import
from .routers import items, users

# global dependencies 선언 - get_query_token
app = FastAPI(dependencies=[Depends(get_query_token)])

# router app 추가
app.include_router(users.router)
app.include_router(items.router)

# router include 함수 호출 매개변수로 APIRouter 정보 추가 가능
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
