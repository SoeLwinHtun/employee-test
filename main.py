from fastapi import FastAPI, Query
from typing import List
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta

app = FastAPI()

# CORS middleware (already correct)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_comments_by_months(months: List[int], year: int):
    conn = sqlite3.connect("company_reports.db")
    cursor = conn.cursor()

    comments = []

    for month in months:
        first_day = datetime(year, month, 1)
        if month == 12:
            last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day = datetime(year, month + 1, 1) - timedelta(days=1)

        cursor.execute('''
            SELECT employee_id, name, department, date, comment 
            FROM employee_comments 
            WHERE date BETWEEN ? AND ?
        ''', (first_day.strftime("%Y-%m-%d"), last_day.strftime("%Y-%m-%d")))

        month_comments = [
            {"EmployeeID": row[0], "Name": row[1], "Department": row[2], "Date": row[3], "Comment": row[4]}
            for row in cursor.fetchall()
        ]

        comments.extend(month_comments)

    conn.close()
    return comments

@app.get("/comments")
def fetch_comments(
    months: List[int] = Query(..., description="Month(s), e.g., 1&months=2"),
    year: int = Query(..., description="Year (YYYY)")
):
    return {"data": get_comments_by_months(months, year)}
