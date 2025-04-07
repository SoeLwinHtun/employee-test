from fastapi import FastAPI, Query
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from datetime import datetime, timedelta

app = FastAPI()

# Allow all origins (you can restrict this later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_comments_by_month(month: int, year: int):
    conn = sqlite3.connect("company_reports.db")
    cursor = conn.cursor()

    # Calculate the first and last day of the given month
    first_day = datetime(year, month, 1).strftime("%Y-%m-%d")
    if month == 12:
        last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = datetime(year, month + 1, 1) - timedelta(days=1)
    last_day = last_day.strftime("%Y-%m-%d")

    # Fetch data for the selected month
    cursor.execute('''
        SELECT employee_id, name, department, date, comment 
        FROM employee_comments 
        WHERE date BETWEEN ? AND ?
    ''', (first_day, last_day))

    comments = [
        {"EmployeeID": row[0], "Name": row[1], "Department": row[2], "Date": row[3], "Comment": row[4]}
        for row in cursor.fetchall()
    ]

    conn.close()
    return comments

@app.get("/comments")
def fetch_comments(month: int = Query(..., description="Month (1-12)"), year: int = Query(..., description="Year (YYYY)")):
    return {"data": get_comments_by_month(month, year)}
