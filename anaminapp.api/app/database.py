import pymongo
from app import config

client = pymongo.mongo_client.MongoClient(config.DATABASE_URL)
print(config.DATABASE_URL)
print('Connected to MongoDB...')
print(config.MONGO_INITDB_DATABASE)
db = client[config.MONGO_INITDB_DATABASE]