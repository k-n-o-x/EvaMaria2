from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Instance
from info import DATABASE_URI, DATABASE_NAME

client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
instance = Instance(db)
