from pydantic import BaseModel


class Request(BaseModel):
    url: str
    params: dict


class Response(BaseModel):
    status_code: int
    content: dict
