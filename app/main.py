import logging
import os

import toml
from fastapi import FastAPI

from core.middlewares import LoggingMiddleware
from api import document_ocr


CURRENT_FILE_PATH = os.path.abspath(os.path.dirname(__file__))
LOG_FILE_PATH = os.path.join(CURRENT_FILE_PATH, "../log/document_ocr.log")

config = toml.load(os.path.join(CURRENT_FILE_PATH, "../configs/config.toml"))

os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

logging.basicConfig(
    format=config["logging"]["format"],
    datefmt=config["logging"]["date_format"],
    level=config["logging"]["level"],
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(),
    ],
)

app = FastAPI()
api_base_path = config["api"]["base_path"]

app.add_middleware(LoggingMiddleware)
app.include_router(document_ocr.router, prefix=api_base_path)
