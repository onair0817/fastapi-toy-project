# from logging_lib import RouterLoggingMiddleware

# import logging.config
# import logging
# import sys

# from fastapi import FastAPI
# from sqlmodel import SQLModel

# # Logging configuration
# logging_config = {
#     "version": 1,
#     "formatters": {
#         "json": {
#             "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
#             "format": "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)s",
#         }
#     },
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "json",
#             "stream": sys.stderr,
#         }
#     },
#     "root": {"level": "DEBUG", "handlers": ["console"], "propagate": True},
# }


# # Define SQLModel for testing
# class User(SQLModel):
#     first_name: str
#     last_name: str
#     email: str


# # Define application
# def get_application() -> FastAPI:
#     application = FastAPI(title="FastAPI Logging", debug=True)

#     return application


# # Logging initialization
# logging.config.dictConfig(logging_config)
# # Initialize application
# app = get_application()
# # Add log middleware
# app.add_middleware(RouterLoggingMiddleware, logger=logging.getLogger(__name__))


# # Root route that returns a User model
# @app.get(
#     "/",
#     response_model=User,
# )
# def root():
#     user = User(first_name="John", last_name="Doe", email="jon@doe.com")
#     return user

# ---

# import logging

# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from starlette.middleware.base import BaseHTTPMiddleware
# from datetime import datetime


# logging.basicConfig(level=logging.INFO)

# app = FastAPI()


# class LoggingMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next):
#         start_time = datetime.now()

#         response = await call_next(request)

#         process_time = (datetime.now() - start_time).total_seconds()
#         formatted_process_time = "{0:.6f}".format(process_time)

#         logging.info(
#             f"{request.method} {request.url} {response.status_code} {formatted_process_time}s"
#         )

#         return response


# app.add_middleware(LoggingMiddleware)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# ---

# from typing import Optional
# from fastapi import Depends, FastAPI


# def query_param_alias(
#     param1: Optional[str] = None, param2: Optional[str] = None
# ) -> Optional[str]:
#     if param1 is not None:
#         return param1
#     elif param2 is not None:
#         return param2
#     else:
#         return None


# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Optional[str] = Depends(query_param_alias)):
#     if q is not None:
#         return {"query": q}
#     else:
#         return {"detail": "No query provided"}


from typing import List, Optional
from pydantic import BaseModel

from fastapi import FastAPI, Request, Form
from starlette.datastructures import FormData

app = FastAPI()


class ImageInfo(BaseModel):
    document_type: Optional[str] = None
    page_number: Optional[int] = None
    img_file: Optional[bytes] = None


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


@app.post("/api/v2/ocr/document", status_code=200, response_model=ImageInfo)
async def document_ocr_req(
    request: Request,
    docType: Optional[str] = Form(None),
    pageNo: Optional[str] = Form(None),
    imgFile: Optional[bytes] = Form(None),
):
    page_no_aliases = [f"imgInfo[{i}].pageNo" for i in range(0, 21)]
    img_file_aliases = [f"imgInfo[{i}].imgFile" for i in range(0, 21)]

    if pageNo is None:
        pageNo = await form_data_alias(request, page_no_aliases)
    if imgFile is None:
        imgFile = await form_data_alias(request, img_file_aliases)

    image_info = ImageInfo()

    image_info.document_type = docType
    if pageNo is not None:
        image_info.page_number = pageNo
    if imgFile is not None:
        image_info.img_file = imgFile

    return image_info
