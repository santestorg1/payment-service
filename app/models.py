from sqlalchemy import Column, String, Float, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Payment(Base):
    __tablename__ = "payments"
    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    processor_id = Column(String)
