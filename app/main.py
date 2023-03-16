import logging
import os
from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, Request, Form, HTTPException
from pydantic import BaseModel
from starlette.datastructures import FormData
from starlette.middleware.base import BaseHTTPMiddleware

CURRENT_FILE_PATH = os.path.abspath(os.path.dirname(__file__))
LOG_FILE_PATH = os.path.join(CURRENT_FILE_PATH, "..", "log", "document_ocr.log")

os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
    handlers=[logging.FileHandler(LOG_FILE_PATH), logging.StreamHandler()],
)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.now()

        try:
            response = await call_next(request)
        except Exception as e:
            logging.exception("An error occurred while processing the request")
            raise HTTPException(status_code=500, detail=str(e))

        process_time = (datetime.now() - start_time).total_seconds()
        formatted_process_time = "{0:.6f}".format(process_time)

        logging.info(
            f"\n[Response Info]\n"
            f"  - Status code: {response.status_code}\n"
            f"  - Process time: {formatted_process_time}s\n"
        )

        return response


class ImageInfo(BaseModel):
    document_type: Optional[str] = None
    page_number: Optional[int] = None
    img_file: Optional[bytes] = None


app = FastAPI()

app.add_middleware(LoggingMiddleware)


def query_param_alias(request: Request, aliases: List[str]) -> Optional[str]:
    for alias in aliases:
        param_value = request.query_params.get(alias)
        if param_value is not None:
            return param_value
    return None


async def form_data_alias(request: Request, aliases: List[str]) -> Optional[str]:
    form_data: FormData = await request.form()
    for alias in aliases:
        if alias in form_data:
            return form_data[alias]
    return None


async def log_request_info(
    request: Request,
    docType: Optional[str],
    pageNo: Optional[int],
    imgFile: Optional[bytes],
):
    logging.info(
        f"\n[Request Info]\n"
        f"  - Method: {request.method}\n"
        f"  - URL: {request.url}\n"
        f"\n[Request Body]\n"
        f"  - docType: {docType}\n"
        f"  - pageNo: {pageNo}\n"
        f"  - imgFile: {imgFile}\n"
    )


async def process_request(
    docType: Optional[str], pageNo: Optional[int], imgFile: Optional[bytes]
) -> ImageInfo:
    image_info = ImageInfo()

    image_info.document_type = docType
    if pageNo is not None:
        image_info.page_number = pageNo
    if imgFile is not None:
        image_info.img_file = imgFile

    return image_info


@app.post("/api/v2/ocr/document", status_code=200, response_model=ImageInfo)
async def document_ocr_request(
    request: Request,
    docType: Optional[str] = Form(None),
    pageNo: Optional[int] = Form(None),
    imgFile: Optional[bytes] = Form(None),
):
    page_no_aliases = [f"imgInfo[{i}].pageNo" for i in range(0, 21)]
    img_file_aliases = [f"imgInfo[{i}].imgFile" for i in range(0, 21)]

    if pageNo is None:
        pageNo_str = await form_data_alias(request, page_no_aliases)
        if pageNo_str is not None:
            pageNo = int(pageNo_str)

    if imgFile is None:
        imgFile = await form_data_alias(request, img_file_aliases)

    await log_request_info(request, docType, pageNo, imgFile)
    image_info = await process_request(docType, pageNo, imgFile)

    return image_info
