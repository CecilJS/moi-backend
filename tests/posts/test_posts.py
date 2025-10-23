import pytest
from httpx import AsyncClient 


@pytest.mark.anyio
async def test_create_post_success(async_client: AsyncClient):
    """Test that creating a post returns 201 and echoes the correct data."""
    
    payload = {"id": 1, "body": "This is a test post"}
    response = await async_client.post("/posts", json=payload)

    response.raise_for_status() 

    assert response.status_code == 201
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["body"] == payload["body"]