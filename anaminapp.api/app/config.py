import os
from dotenv import load_dotenv
load_dotenv()

MONGO_INITDB_DATABASE = os.getenv("MONGO_INITDB_DATABASE")
DATABASE_URL = os.getenv("DATABASE_URL")
CLIENT_ORIGIN = os.getenv("CLIENT_ORIGIN")