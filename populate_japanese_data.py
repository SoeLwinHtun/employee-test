import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random

# Connect to SQLite database
conn = sqlite3.connect("company_reports.db")
cursor = conn.cursor()

# Departments for variety
departments = ["IT部", "人事部", "経理部", "マーケティング部"]

# Dummy Japanese comments by sentiment
positive_comments = [
    "最近の仕事がとても楽しいです。",
    "チームの雰囲気がとても良いです。",
    "上司がサポートしてくれて助かっています。",
    "働きやすい環境に感謝しています。",
    "今月は成果も上がり、満足しています。"
]

negative_comments = [
    "最近、仕事のストレスが多いです。",
    "残業が多くて体調が心配です。",
    "上司とのコミュニケーションがうまくいっていません。",
    "モチベーションが下がっています。",
    "評価に納得できませんでした。"
]

neutral_comments = [
    "通常通りの業務をこなしています。",
    "今月は特に大きな変化はありません。",
    "新しいプロジェクトが始まりました。",
    "普通に働いています。",
    "来月の予定を立てています。"
]

# Merge and tag them for better sentiment variety
all_comments = positive_comments + negative_comments + neutral_comments

# Starting from Jan 2024 to Mar 2025
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 3, 1)

current_date = start_date

while current_date <= end_date:
    for _ in range(10):  # 10 rows per month
        day = random.randint(1, 28)  # Safe day range
        date_str = current_date.replace(day=day).strftime("%Y-%m-%d")
        comment = random.choice(all_comments)
        cursor.execute('''
            INSERT INTO employee_comments (employee_id, name, department, date, comment)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            random.randint(100, 200),
            f"社員{random.randint(1, 50)}",
            random.choice(departments),
            date_str,
            comment
        ))
    current_date += relativedelta(months=1)

conn.commit()
conn.close()
print("Japanese dummy data added for Jan 2024 – Mar 2025!")
