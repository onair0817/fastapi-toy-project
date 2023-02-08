from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class OutputData(BaseModel):
    result: str
    type: str
    created_at: str


class InputData(BaseModel):
    text: str
    type: str
    created_at: str


@app.post("/convert")
async def convert(data: InputData):
    text = data.text
    type = data.type
    created_at = data.created_at
    # Perform your text conversion here
    result = text.upper()
    return OutputData(result=result, type=type, created_at=created_at)
