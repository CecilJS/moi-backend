from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from main import app
from httpx import AsyncClient, ASGITransport
import pytest_asyncio
from core.database import Base, engine, async_session_factory

# 1. Ensure tables are created ONCE per session
@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    # Dispose engine to avoid "coroutine never awaited" warnings
    await engine.dispose()

# 2. Use function-scoped sessions for individual tests
@pytest_asyncio.fixture()
async def db():
    async with async_session_factory() as session:
        async with session.begin():
            yield session
            await session.rollback()

# 3. Async client that uses the session
@pytest_asyncio.fixture()
async def async_client(db: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac