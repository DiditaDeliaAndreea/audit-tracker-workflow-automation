from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

DATABASE = BASE_DIR / "database" / "connecthub_demo.db"
SQL_FILE = BASE_DIR / "sql" / "filter_reports.sql"


def extract_reports() -> pd.DataFrame:
    """
    Executes the SQL query and returns the filtered reports.
    """

    conn = sqlite3.connect(DATABASE)

    with open(SQL_FILE, "r") as file:
        query = file.read()

    reports_df = pd.read_sql_query(query, conn)

    conn.close()

    return reports_df


if __name__ == "__main__":

    reports = extract_reports()

    print("=" * 60)
    print("REPORTS RETRIEVED")
    print("=" * 60)

    print(reports)

    print(f"\nTotal reports: {len(reports)}")