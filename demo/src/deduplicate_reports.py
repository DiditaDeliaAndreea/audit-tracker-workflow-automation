import pandas as pd


def remove_existing_reports(
    tracker_df: pd.DataFrame,
    existing_issue_numbers: list[int]
) -> pd.DataFrame:
    """
    Removes reports that already exist in the audit tracker.

    Args:
        tracker_df:
            Data prepared for export.

        existing_issue_numbers:
            Issue numbers already present in the tracker.

    Returns:
        DataFrame containing only new reports.
    """

    if not existing_issue_numbers:
        return tracker_df.reset_index(drop=True)

    new_reports = tracker_df[
        ~tracker_df["Issue Number"].isin(existing_issue_numbers)
    ]

    return new_reports.reset_index(drop=True)