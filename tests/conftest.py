import os
import pytest
from fastapi.testclient import TestClient 
from typing import AsyncGenerator, Generator
from httpx import (
    AsyncClient,
    ASGITransport,
) 
os.environ["ENV_STATE"] = "test" # TODO: Implement .env setup (#4)

# TODO: Implement database setup (#3)
from database import database #noqa: E402 

# TODO: Implement main logic (#2)
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
    yield
    await database.disconnect()

@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
