import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_create_post_success(async_client: AsyncClient):
    payload = {"body": "This is a test post"}  # Remove "id": 1
    response = await async_client.post("/posts", json=payload)

    response.raise_for_status()
    assert response.status_code == 201

    response_data = response.json()
    assert "id" in response_data
    assert isinstance(response_data["id"], int)
    assert response_data["body"] == payload["body"]