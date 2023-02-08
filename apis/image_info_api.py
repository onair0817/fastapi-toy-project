from typing import List
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from PIL import Image

app = FastAPI()


class ImageInfo(BaseModel):
    filename: str
    format: str
    size: List[int]
    mode: str


@app.post("/image/process")
async def process_image(file: UploadFile):
    image = Image.open(file.file)
    return ImageInfo(
        filename=file.filename,
        format=image.format,
        size=list(image.size),
        mode=image.mode,
    )
