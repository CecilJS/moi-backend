from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck", tags=["Health"])
async def healthcheck():
    """
    Simple healthcheck endpoint to verify the API is running.
    """
    return {"status": "ok"}
