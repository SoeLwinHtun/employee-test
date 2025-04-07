import sqlite3
from datetime import datetime
import random

# Connect to SQLite database (or create if not exists)
conn = sqlite3.connect("company_reports.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee_comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        name TEXT,
        department TEXT,
        date TEXT,
        comment TEXT
    )
''')

departments = ["IT", "HR", "Finance", "Marketing"]
comments = [
    "Feeling overwhelmed with work.",
    "Loving my tasks recently!",
    "I think there’s too much workload.",
    "Great work-life balance.",
    "I feel unsupported in my role.",
    "Everything is running smoothly!",
]

# Generate data for Jan 2024 to Mar 2025
start_year = 2024
end_year = 2025
end_month = 3

for year in range(start_year, end_year + 1):
    month_range = range(1, 13) if year < end_year else range(1, end_month + 1)

    for month in month_range:
        for _ in range(10):  # 10 entries per month
            day = random.randint(1, 28)  # To avoid invalid dates
            date = datetime(year, month, day).strftime("%Y-%m-%d")

            cursor.execute('''
                INSERT INTO employee_comments (employee_id, name, department, date, comment)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                random.randint(100, 200),
                f"Employee {random.randint(1, 50)}",
                random.choice(departments),
                date,
                random.choice(comments),
            ))

# Commit and close
conn.commit()
conn.close()

print("Database populated with dummy data from Jan 2024 to Mar 2025.")
