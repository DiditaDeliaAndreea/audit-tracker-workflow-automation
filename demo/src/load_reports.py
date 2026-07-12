from pathlib import Path
import sqlite3

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_PATH = BASE_DIR / "database" / "connecthub_demo.db"


def load_reports(sql_query: str) -> pd.DataFrame:
    """
    Execute a SQL query against the demo database and
    return the results as a Pandas DataFrame.
    """

    with sqlite3.connect(DATABASE_PATH) as connection:
        reports_df = pd.read_sql_query(
            sql_query,
            connection,
        )

    return reports_df