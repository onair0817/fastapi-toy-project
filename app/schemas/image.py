from typing import Optional
from pydantic import BaseModel


class ImageInfo(BaseModel):
    document_type: Optional[str] = None
    page_number: Optional[int] = None
    img_file: Optional[bytes] = None
