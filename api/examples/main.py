from logging_lib import RouterLoggingMiddleware

import logging.config
import logging
import sys

from fastapi import FastAPI
from sqlmodel import SQLModel

# Logging configuration
logging_config = {
    "version": 1,
    "formatters": {
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)s",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": sys.stderr,
        }
    },
    "root": {"level": "DEBUG", "handlers": ["console"], "propagate": True},
}


# Define SQLModel for testing
class User(SQLModel):
    first_name: str
    last_name: str
    email: str


# Define application
def get_application() -> FastAPI:
    application = FastAPI(title="FastAPI Logging", debug=True)

    return application


# Logging initialization
logging.config.dictConfig(logging_config)
# Initialize application
app = get_application()
# Add log middleware
app.add_middleware(RouterLoggingMiddleware, logger=logging.getLogger(__name__))


# Root route that returns a User model
@app.get(
    "/",
    response_model=User,
)
def root():
    user = User(first_name="John", last_name="Doe", email="jon@doe.com")
    return user
