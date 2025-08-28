import sys
import os

sys.path.append(os.path.join(os.getcwd(), "."))

from fastapi import FastAPI

from app.routers.todo import todo_router

app = FastAPI()

app.include_router(todo_router)
