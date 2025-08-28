import sys
import os

from sqlalchemy import Null
from sqlalchemy.ext.asyncio import AsyncSession

sys.path.append(os.path.join(os.getcwd(), "."))

from typing import Optional

from fastapi import Depends

from loguru import logger

from app.database.models import Task
from app.configs.sqlite import get_async_session


class TodoRepository:
    db: AsyncSession

    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        self.db = db

    async def create_task(self, title: str, description: str = None):
        try:
            task = Task(title=title, description=description, is_completed=False)
            self.db.add(task)
            await self.db.commit()
            await self.db.refresh(task)
            return task
        except Exception as e:
            await self.db.rollback()
            logger.error(f"Error with create task: {e}")
            raise
