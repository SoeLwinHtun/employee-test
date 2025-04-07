import sqlite3

# Connect to database (it will be created if it doesn't exist)
conn = sqlite3.connect("employee_skills.db")
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    language TEXT NOT NULL,
    database TEXT NOT NULL,
    framework TEXT NOT NULL                      
)
""")
conn.commit()
conn.close()
