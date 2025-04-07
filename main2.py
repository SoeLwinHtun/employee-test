from fastapi import FastAPI, Query
import sqlite3
import json
from typing import List

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect("employee_skills.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/employees")
def get_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    conn.close()

    employees = []
    for row in rows:
        try:
            # Safely parse JSON or use empty list if parsing fails
            language = json.loads(row["language"]) if row["language"] else []
            database = json.loads(row["database"]) if row["database"] else []
            framework = json.loads(row["framework"]) if row["framework"] else []
        except json.JSONDecodeError:
            # In case of malformed JSON, use empty lists
            language, database, framework = [], [], []

        employees.append({
            "id": row["id"],
            "name": row["name"],
            "language": language,
            "database": database,
            "framework": framework
        })

    return {"employees": employees}
