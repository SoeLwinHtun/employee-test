import sqlite3
from datetime import datetime, timedelta
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

# Generate six months of data
departments = ["IT", "HR", "Finance", "Marketing"]
comments = [
    "Feeling overwhelmed with work.",
    "Loving my tasks recently!",
    "I think there’s too much workload.",
    "Great work-life balance.",
    "I feel unsupported in my role.",
    "Everything is running smoothly!",
]

# Insert dummy data
today = datetime.today()
for i in range(180):  # 6 months (30 days * 6)
    date = today - timedelta(days=i)
    cursor.execute('''
        INSERT INTO employee_comments (employee_id, name, department, date, comment)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        random.randint(100, 200),
        f"Employee {random.randint(1, 50)}",
        random.choice(departments),
        date.strftime("%Y-%m-%d"),
        random.choice(comments),
    ))

# Commit and close
conn.commit()
conn.close()

print("Database setup complete with six months of dummy data!")
