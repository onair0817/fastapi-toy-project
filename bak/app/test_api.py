from models import DocumentSchema, KeyValueServer, Logger

from fastapi import FastAPI, Request, Response
from starlette.background import BackgroundTask
from starlette.types import Message

import json
import logging

app = FastAPI()

Logger(target="test_api")


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    def log_info(req_body, res_body):
        logging.info(req_body)
        logging.info(res_body)

    async def set_body(request: Request, body: bytes):
        async def receive() -> Message:
            return {"type": "http.request", "body": body}

        request._receive = receive

    req_body = await request.body()
    await set_body(request, req_body)
    response = await call_next(request)

    res_body = b""
    async for chunk in response.body_iterator:
        res_body += chunk

    task = BackgroundTask(log_info, req_body, res_body)
    # task = BackgroundTask(log_info, req_body, res_body)
    return Response(
        content=res_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type,
        background=task,
    )


@app.post("/document/ocr")
async def process_document(document: DocumentSchema):
    # OCR
    ocr_rst = {}
    key_value_server = ""
    # with open("./contract_000300.json", "r") as rst:
    #     ocr_rst = json.loads(rst)
    # KEY-VALUE
    if document and document.type == "contract":
        key_value_server = KeyValueServer(document.type)

    return DocumentSchema(
        type=document.type,
        description=document.description,
        page=document.page,
        ocr=json.dumps(ocr_rst),
        key_value=key_value_server,
    )
