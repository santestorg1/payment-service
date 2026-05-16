import pytest
from app.main import app
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_get_payments():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.get("/payments?user_id=test123")
        assert resp.status_code == 200

@pytest.mark.asyncio
async def test_process_payment():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/payments/process", json={"amount": 99.99, "card_token": "tok_test"})
        assert resp.status_code == 200
        assert resp.json()["status"] == "processed"
