from fastapi import FastAPI, HTTPException
from .database import get_db

app = FastAPI()

@app.get("/students")
def get_students():
    try:
        with get_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name, program FROM students")
                return {"students": cur.fetchall()}
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@app.get("/subjects")
def get_subjects():
    try:
        with get_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name, year FROM subjects ORDER BY year")
                return {"subjects": cur.fetchall()}
    except Exception as e:
        raise HTTPException(500, detail=str(e))