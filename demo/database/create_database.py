from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "connecthub_demo.db"

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE user_reports (
    report_id TEXT,
    issue_id TEXT,
    created_date TEXT,
    team TEXT,
    area TEXT,
    title TEXT,
    tags TEXT,
    status TEXT
)
""")

reports = [
    ("REP-1001", "ISSUE-48321", "2026-06-29 09:15:00", "Trust & Safety", "User Reports", "Spam Account", "review,spam", "Open"),
    ("REP-1002", "ISSUE-48322", "2026-06-29 14:30:00", "Moderation", "User Reports", "Offensive Content", "review,abuse", "Open"),
    ("REP-1003", "ISSUE-48323", "2026-06-30 10:20:00", "Engineering", "Mobile App", "App Crash", "bug,mobile", "Open"),
    ("REP-1004", "ISSUE-48324", "2026-06-30 16:45:00", "Billing", "Payments", "Payment Failure", "review,payment", "Open"),
    ("REP-1005", "ISSUE-48325", "2026-07-01 08:10:00", "Trust & Safety", "User Reports", "Fake Profile", "review,fraud", "Closed"),
    ("REP-1006", "ISSUE-48326", "2026-07-01 13:40:00", "Moderation", "User Reports", "Harassment Report", "review,priority", "Open"),
    ("REP-1007", "ISSUE-48327", "2026-07-02 11:05:00", "Engineering", "Backend", "API Timeout", "backend", "Open"),
    ("REP-1008", "ISSUE-48328", "2026-07-03 15:25:00", "Trust & Safety", "User Reports", "Fake Giveaway", "review,scam", "Open"),
    ("REP-1009", "ISSUE-48329", "2026-07-04 12:00:00", "Billing", "Payments", "Refund Request", "payment", "Closed"),
    ("REP-1010", "ISSUE-48330", "2026-07-05 09:30:00", "Moderation", "User Reports", "Impersonation", "review,identity", "Open")
]

cursor.executemany("""
INSERT INTO user_reports
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", reports)

conn.commit()
conn.close()

print("Database created successfully.")