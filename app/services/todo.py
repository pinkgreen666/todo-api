import sys
import os

sys.path.append(os.path.join(os.getcwd(), "."))

from fastapi import Depends
from app.repositories.todo import TodoRepository


class TodoService:
    todo_repository: TodoRepository

    def __init__(self, todo_repository: TodoRepository = Depends()) -> None:
        self.todo_repository = todo_repository

    async def create_task(self, title: str, description: str = None):
        task = await self.todo_repository.create_task(
            title=title, description=description
        )
        return task

    async def delete_task(self, task_id: int):
        await self.todo_repository.delete_task(task_id=task_id)
