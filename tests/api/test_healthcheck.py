import pytest
from httpx import AsyncClient


async def health_status(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.get("/healthcheck")
    return response.json()


@pytest.fixture()
async def get_health_status(async_client: AsyncClient):
    return await health_status("Health Check", async_client)


@pytest.mark.anyio
async def test_healthcheck(async_client: AsyncClient):
    response = await async_client.get("/healthcheck")
    print(response)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
