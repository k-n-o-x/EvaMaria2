from pymongo import MongoClient
from umongo import Instance
from motor.motor_asyncio import AsyncIOMotorClient
from info import DATABASE_URI, DATABASE_NAME

# Create a motor client
client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]

# Create the umongo instance
instance = Instance(db)

def init_db():
    return db
