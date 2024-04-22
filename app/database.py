import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://shubhendra:shubh@localhost:5432/youtubeblend"

if not DATABASE_URL.startswith("postgresql+asyncpg://"):
    raise ValueError(
        "DATABASE_URL must be compatible with async SQLAlchemy and asyncpg"
    )

try:
    async_engine = create_async_engine(
        DATABASE_URL, pool_recycle=3600, echo=True, echo_pool="debug"
    )
    AsyncSessionLocal = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
except Exception as e:
    raise ValueError(f"Failed to create engine and session: {e}")


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as db:
        yield db
