from models import Logger, ImageInfo  # , Document

from fastapi import FastAPI, UploadFile, Request, Response
from starlette.background import BackgroundTask
from PIL import Image

app = FastAPI()
logger = Logger(target="image_info_api", filename="info.log")


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    req_body = await request.body()
    await logger.set_body(request, req_body)
    response = await call_next(request)

    res_body = b""
    async for chunk in response.body_iterator:
        res_body += chunk

    task = BackgroundTask(logger.get_info, req_body, res_body)
    return Response(
        content=res_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type,
        background=task,
    )


@app.post("/image/process")
async def process_image(file: UploadFile, document: dict = None):
    nxt = ""
    if document and document.type == "a":
        nxt = document.get("seq", [])[0] if document.get("seq") else None
        print(nxt)
    image = Image.open(file.file)
    return ImageInfo(
        nxt=nxt,
        filename=file.filename,
        format=image.format,
        size=list(image.size),
        mode=image.mode,
    )
