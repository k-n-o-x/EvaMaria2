from motor.motor_asyncio import AsyncIOMotorClient
from models import instance  # This is your MotorAsyncIOInstance

from info import DATABASE_URI, DATABASE_NAME

client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
instance.init(db)  # <-- This is the correct way to bind the DB
