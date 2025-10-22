import os
import pytest
from fastapi.testclient import TestClient 
from typing import AsyncGenerator, Generator
from httpx import (
    AsyncClient,
    ASGITransport,
) 
os.environ["ENV_STATE"] = "test" 

from core.database import database #noqa: E402 

from main import app  # noqa: E402 



@pytest.fixture(scope="session") 
def anyio_backend():
    return "asyncio"

@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    await database.connect()
    transaction = await database.transaction()
    try:
        yield
    finally:
        await transaction.rollback()
        await database.disconnect()

@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
