import sys
import os

sys.path.append(os.path.join(os.getcwd(), "."))

from typing import Optional
from fastapi import APIRouter, Depends

from app.services.todo import TodoService

todo_router = APIRouter(prefix="/api/v1/todo")


@todo_router.post("/create_task")
async def create_task(
    title: str, description: Optional[str], todo_service: TodoService = Depends()
):
    task = await todo_service.create_task(title=title, description=description)
    return {"msg": "ok"}


@todo_router.delete("/delete_task")
async def delete_task(task_id: int, todo_service: TodoService = Depends()):
    await todo_service.delete_task(task_id=task_id)
    return {"msg": "ok"}

@todo_router.get("/")
async def get_all_tasks(todo_service: TodoService = Depends()):
    tasks = await todo_service.get_all_tasks()
    return tasks

@todo_router.post("/complete_task")
async def complete_task(task_id: int, is_complet: bool, todo_service: TodoService = Depends()):
    print(is_complet)
    await todo_service.complete_task(task_id=task_id, is_complet=is_complet)
    return {"msg": "ok"}
