import logging
from datetime import datetime

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware


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
