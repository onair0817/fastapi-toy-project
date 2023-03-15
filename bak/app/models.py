from enum import Enum
from pydantic import BaseModel
from typing import Optional, Json, Any

import logging


class KeyValueServer(Enum):
    contract = "contract"


class DocumentSchema(BaseModel):
    type: str
    description: Optional[str] = None
    page: int
    ocr: Optional[Json[Any]] = None
    key_value: Optional[Enum] = None


class Logger:
    def __init__(self, target, filename="log/info.log", level=logging.DEBUG):
        self._logger = logging.getLogger(target)
        self._logger.setLevel(level)  # or logging.basicConfig(level=level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        stream_handler = logging.StreamHandler().setFormatter(formatter)
        self._logger.addHandler(stream_handler)
        file_handler = logging.FileHandler(filename, mode="w")
        self._logger.addHandler(file_handler)
