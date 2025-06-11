from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client['rbac_app']