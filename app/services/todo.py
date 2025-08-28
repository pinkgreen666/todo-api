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

    async def get_all_tasks(self):
        tasks = await self.todo_repository.get_all_task()
        print(tasks)
        return tasks

    async def complete_task(self, task_id: int, is_complet: bool):
        await self.todo_repository.complete_task(task_id=task_id, is_complet=is_complet)
