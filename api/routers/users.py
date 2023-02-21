from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"], status_code=200)
async def read_users() -> list:
    return [{"username": "Ted"}, {"username": "Robin"}]


@router.get("/users/me", tags=["users"], status_code=200)
async def read_user_me() -> dict:
    return {"username": "fakecurrentuser"}
