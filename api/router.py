from fastapi import APIRouter

from api.endpoints.posts import router as posts_router
from api.endpoints.healthcheck import router as healthcheck_router

api_router = APIRouter()
api_router.include_router(posts_router)
api_router.include_router(healthcheck_router)