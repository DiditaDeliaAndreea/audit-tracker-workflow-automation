import sqlite3
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE = BASE_DIR / "data" / "connecthub_demo.db"
SQL_FILE = BASE_DIR / "sql" / "filter_reports.sql"

# Connect to database
conn = sqlite3.connect(DATABASE)

# Read SQL query
with open(SQL_FILE, "r") as file:
    query = file.read()

# Execute query
reports_df = pd.read_sql_query(query, conn)

conn.close()

print(reports_df)