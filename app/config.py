import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/payments")
    STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY", "")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

settings = Settings()
