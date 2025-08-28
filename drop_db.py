from app.configs.sqlite import drop_db
import asyncio


asyncio.run(drop_db())
