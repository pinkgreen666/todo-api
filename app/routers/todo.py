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
