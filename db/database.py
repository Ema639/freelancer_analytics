import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
if DB_URL is None:
    raise ValueError("DATABASE_URL не найден в .env")

engine = create_engine(DB_URL)
