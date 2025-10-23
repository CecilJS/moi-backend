import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_healthcheck(async_client: AsyncClient):
    response = await async_client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json().get("status") == "ok"
