from typing import Optional

from fastapi import APIRouter, Request, Form

from schemas.image import ImageInfo
from utils.helpers import (
    form_data_alias,
    log_request_info,
    process_request,
)

router = APIRouter()


@router.post("/api/v2/ocr/document", status_code=200, response_model=ImageInfo)
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
