import sys
import os

from sqlalchemy import Null, delete, select, text
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

    async def delete_task(self, task_id: int):
        try:
            query = delete(Task).where(Task.id == task_id)
            await self.db.execute(query)
            await self.db.commit()

        except Exception as e:
            await self.db.rollback()
            logger.error(f"Error with delete task: {e}")
            raise

    async def get_all_task(self):
        try:
            query = select(Task)
            result = (await self.db.execute(query)).scalars().all()
            return result
        except Exception as e:
            logger.error(f"Error with get all tasks: {e}")
            return None
