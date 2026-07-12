from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd


BASE_ISSUE_URL = "https://connecthub.demo/issues/"
OBSERVATIONS_TEMPLATE = (
    "Review the reported issue and document the audit findings here."
)


def generate_hyperlink(issue_id: str) -> str:
    """Create a clickable Excel hyperlink formula."""
    issue_url = f"{BASE_ISSUE_URL}{issue_id}"
    return f'=HYPERLINK("{issue_url}", "{issue_id}")'


def prepare_tracker_data(reports_df: pd.DataFrame) -> pd.DataFrame:
    """Prepare filtered reports in the audit tracker format."""

    tracker_df = reports_df.copy()

    tracker_df["Exported Date"] = datetime.now(
        ZoneInfo("Europe/Dublin")
    ).strftime("%Y-%m-%d")

    tracker_df["Issue"] = tracker_df["issue_id"].apply(generate_hyperlink)
    tracker_df["Auditor Name"] = ""
    tracker_df["Team Name"] = tracker_df["team"]
    tracker_df["Area"] = tracker_df["area"]
    tracker_df["Audit Outcome"] = ""
    tracker_df["Observations"] = OBSERVATIONS_TEMPLATE

    return tracker_df[
        [
            "Exported Date",
            "Issue",
            "Auditor Name",
            "Team Name",
            "Area",
            "Audit Outcome",
            "Observations",
        ]
    ]