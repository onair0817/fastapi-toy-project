import logging

from typing import List, Optional
from fastapi import Request
from starlette.datastructures import FormData

from schemas.image import ImageInfo


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
