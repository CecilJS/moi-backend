from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.database import engine
from api.router import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()

def create_application():
    application = FastAPI(lifespan=lifespan)
    application.include_router(api_router)
    return application

app = create_application()