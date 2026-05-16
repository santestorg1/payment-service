from fastapi import FastAPI, Query
from sqlalchemy import text
from app.database import engine

app = FastAPI(title="Payment Service")

@app.get("/payments")
async def get_payments(user_id: str = Query(...)):
    # VULNERABILITY: SQL Injection
    query = f"SELECT * FROM payments WHERE user_id = '{user_id}'"
    async with engine.connect() as conn:
        result = await conn.execute(text(query))
        return result.fetchall()

@app.post("/payments/process")
async def process_payment(amount: float, card_token: str):
    # Process payment via Stripe
    return {"status": "processed", "amount": amount}
