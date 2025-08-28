import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database.models import Base

async_engine = create_async_engine("sqlite+aiosqlite:///test.db", echo=True)

async_session = async_sessionmaker(
    bind=async_engine, expire_on_commit=False, autocommit=False
)


async def get_async_session():
    async with async_session() as session:
        yield session


async def create_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
