import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load env variables
load_dotenv()
MONGO_URL = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("DB_NAME")

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(MONGO_URL)
    print("Connected to MongoDB")

async def close_mongo_connection():
    db.client.close()
    print("Closed MongoDB connection")

def get_database():
    return db.client[DB_NAME]