from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from core.config import config
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

engine = create_async_engine(config.DATABASE_URL, echo=True)

async_session_factory = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)