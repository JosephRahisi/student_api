    # app/database.py
import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "studentdb1"),
        user=os.getenv("DB_USER", "api_user1"),
        password=os.getenv("DB_PASS", "2020"),
        cursor_factory=RealDictCursor
    )