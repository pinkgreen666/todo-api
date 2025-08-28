import asyncio
from app.configs.sqlite import create_db


asyncio.run(create_db())
