import logging
import os

from fastapi import FastAPI

from core.middlewares import LoggingMiddleware
from api import document_ocr


CURRENT_FILE_PATH = os.path.abspath(os.path.dirname(__file__))
LOG_FILE_PATH = os.path.join(CURRENT_FILE_PATH, "../..", "log", "document_ocr.log")

os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
    handlers=[logging.FileHandler(LOG_FILE_PATH), logging.StreamHandler()],
)


app = FastAPI()

app.add_middleware(LoggingMiddleware)
app.include_router(document_ocr.router)
