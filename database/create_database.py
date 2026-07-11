import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE tasks (
    task_id TEXT,
    title TEXT,
    status TEXT,
    severity TEXT,
    team TEXT,
    task_url TEXT
)
""")

tasks = [
    ("TASK-101", "Payment validation", "Open", "High", "Alpha", "https://demo/tasks/101"),
    ("TASK-102", "Invoice review", "Closed", "Low", "Beta", "https://demo/tasks/102"),
    ("TASK-103", "User access audit", "Open", "High", "Alpha", "https://demo/tasks/103"),
    ("TASK-104", "Policy review", "Open", "Medium", "Gamma", "https://demo/tasks/104"),
    ("TASK-105", "KYC verification", "Open", "High", "Beta", "https://demo/tasks/105"),
]

cursor.executemany(
    "INSERT INTO tasks VALUES (?,?,?,?,?,?)",
    tasks
)

conn.commit()
conn.close()
