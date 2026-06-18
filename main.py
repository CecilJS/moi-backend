from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.database import database
from api.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


def create_application():
    application = FastAPI()

    application.include_router(api_router)

    return application


app = create_application()