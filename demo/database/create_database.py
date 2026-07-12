import sqlite3

conn = sqlite3.connect("connecthub_demo.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE user_reports (
    report_id TEXT,
    issue_id TEXT,
    reported_at TEXT,
    reported_by TEXT,
    issue_type TEXT,
    severity TEXT,
    status TEXT,
    assigned_team TEXT
)
""")

reports = [
    ("REP-1001", "ISSUE-48321", "2026-07-01", "user_125", "Spam Account", "High", "Open", "Trust & Safety"),
    ("REP-1002", "ISSUE-48322", "2026-07-01", "user_482", "Offensive Content", "Medium", "Open", "Moderation"),
    ("REP-1003", "ISSUE-48323", "2026-07-01", "user_876", "Login Issue", "Low", "Closed", "Support"),
    ("REP-1004", "ISSUE-48324", "2026-07-02", "user_932", "Fake Profile", "High", "Open", "Trust & Safety"),
    ("REP-1005", "ISSUE-48325", "2026-07-02", "user_341", "App Crash", "High", "Open", "Engineering"),
    ("REP-1006", "ISSUE-48326", "2026-07-02", "user_777", "Payment Error", "Medium", "Open", "Billing"),
    ("REP-1007", "ISSUE-48327", "2026-07-02", "user_298", "Harassment Report", "High", "Open", "Moderation"),
    ("REP-1008", "ISSUE-48328", "2026-07-03", "user_615", "Fake Giveaway", "Medium", "Closed", "Trust & Safety"),
    ("REP-1009", "ISSUE-48329", "2026-07-03", "user_511", "Impersonation", "High", "Open", "Trust & Safety"),
    ("REP-1010", "ISSUE-48330", "2026-07-03", "user_890", "Profile Picture Violation", "Medium", "Open", "Moderation")
]

cursor.executemany("""
INSERT INTO user_reports
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", reports)

conn.commit()
conn.close()

print("Database created successfully.")
