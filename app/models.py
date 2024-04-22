import asyncio
from datetime import datetime as dt

import pytz
from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String, UniqueConstraint, func)
from sqlalchemy.orm import declarative_base

timezone = pytz.timezone("Asia/Kolkata")
Base = declarative_base()
from app.database import async_engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    google_id = Column(String)
    name = Column(String)
    email = Column(String)
    picture = Column(String)
    access_token = Column(String)
    refresh_token = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=dt.now(timezone)
    )


class Blend(Base):
    __tablename__ = "blends"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    is_deleted = Column(Boolean, server_default="0", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=dt.now(timezone)
    )
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)


class BlendUserMap(Base):
    __tablename__ = "blend_user_map"

    blend_id = Column(Integer, ForeignKey("blends.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)


class BlendScore(Base):
    __tablename__ = "blend_scores"

    id = Column(Integer, primary_key=True)
    blend_id = Column(Integer, ForeignKey("blends.id"), nullable=False)
    user_id_1 = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_id_2 = Column(Integer, ForeignKey("users.id"), nullable=False)
    score = Column(Float)  # Score between 0 and 1

    __table_args__ = (UniqueConstraint("blend_id", "user_id_1", "user_id_2"),)


async def create_tables():
    async with async_engine.begin() as conn:
        # Use `run_sync` to run `Base.metadata.create_all` within an async context
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(create_tables())
