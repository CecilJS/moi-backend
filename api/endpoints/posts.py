from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.posts import UserPostIn, UserPost
from models.posts import Post
from core.deps import get_db

router = APIRouter()

@router.post("/posts", response_model=UserPost, status_code=status.HTTP_201_CREATED, tags=["Posts"])
async def create_posts(post: UserPostIn, db: AsyncSession = Depends(get_db)):
    new_post = Post(**post.model_dump())

    db.add(new_post)
    await db.commit()

    await db.refresh(new_post)

    return new_post