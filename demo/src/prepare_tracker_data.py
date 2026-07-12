import re
import pandas as pd

BASE_ISSUE_URL = "https://connecthub.demo/issues/"


def generate_hyperlink(issue_id: str) -> str:
    """
    Creates a Google Sheets / Excel hyperlink.
    """

    return f'=HYPERLINK("{BASE_ISSUE_URL}{issue_id}", "{issue_id}")'


def extract_issue_number(issue_id: str) -> int:
    """
    ISSUE-48321 -> 48321
    """

    match = re.search(r"\d+", issue_id)

    if match:
        return int(match.group())

    return None


def prepare_tracker_data(reports_df: pd.DataFrame) -> pd.DataFrame:
    """
    Builds the dataframe that will be exported
    to the audit tracker.
    """

    tracker_df = reports_df.copy()

    tracker_df["Issue Number"] = (
        tracker_df["issue_id"]
        .apply(extract_issue_number)
    )

    tracker_df["Issue"] = (
        tracker_df["issue_id"]
        .apply(generate_hyperlink)
    )

    tracker_df = tracker_df[
        [
            "Issue Number",
            "Issue",
            "created_date",
            "team",
            "area",
            "title",
            "tags",
        ]
    ]

    tracker_df.columns = [
        "Issue Number",
        "Issue",
        "Created Date",
        "Team",
        "Area",
        "Title",
        "Tags",
    ]

    return tracker_df