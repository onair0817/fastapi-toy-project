import logging
import random
import string
import time

from fastapi import FastAPI, Request

# logging.config.fileConfig("logging.conf", disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)
    logger.info(
        f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}"
    )

    return response


@app.get("/")
async def root():
    logger.info("logging from the root logger")
    return {"status": "alive"}


# @app.post("/api/v2/ocr/document", status_code=200)
# async def call_ocr(param1: str, param2: str):
#     # if imgInfo:
#     #     results = {"docType": docType, "imgInfo": imgInfo}
#     # else:
#     #     results = {"docType": docType}
#     results = {"docType": param1, "pageNo": param2}
#     return results


# @app.post("/api/v2/ocr/document", status_code=200)
# async def post_item(
#     *, docType: str = Form(...), pageNo: str = Form(...), imgFile: bytes = File()
# ):
#     results = {"docType": docType, "pageNo": pageNo, "imgFile": imgFile}
#     return results


"""
curl --location 'http://127.0.0.1:8001/api/v2/ocr/document' \
--form 'docType="\"D53\""' \
--form 'pageNo="\"0\""' \
--form 'imgFile="\"a\""'
"""
