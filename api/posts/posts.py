from fastapi import APIRouter, status
from models.posts import UserPostIn, UserPost
from core.database import post_table, database

router = APIRouter()


@router.post("/posts",  response_model=UserPost, status_code=status.HTTP_201_CREATED, tags=["Posts"])
async def create_posts(post: UserPostIn):
    """
    Creating a successful post returns 201 and echoes the correct data..
    """
    data = post.model_dump()
    query = post_table.insert().values(data)
    last_record_id = await database.execute(query)
    return {**data, 'id': last_record_id }