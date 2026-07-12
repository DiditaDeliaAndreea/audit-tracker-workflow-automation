import re

import pandas as pd


def extract_issue_id_from_formula(formula: str) -> str | None:
    """Extract ISSUE-12345 from an Excel hyperlink formula."""
    match = re.search(r'"(ISSUE-\d+)"\)$', str(formula))
    return match.group(1) if match else None


def remove_existing_reports(
    tracker_df: pd.DataFrame,
    existing_issue_ids: set[str],
) -> pd.DataFrame:
    """Keep only issues not already present in the tracker."""

    issue_ids = tracker_df["Issue"].apply(extract_issue_id_from_formula)

    new_reports = tracker_df[
        ~issue_ids.isin(existing_issue_ids)
    ]

    return new_reports.reset_index(drop=True)