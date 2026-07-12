import pandas as pd


def group_by_team(df: pd.DataFrame) -> dict:
    """
    Splits the dataframe into one dataframe per team.
    """

    grouped_reports = {}

    for team, team_df in df.groupby("team"):
        grouped_reports[team] = team_df.reset_index(drop=True)

    return grouped_reports


if __name__ == "__main__":

    from extract_reports import extract_reports

    reports = extract_reports()

    grouped = group_by_team(reports)

    for team, data in grouped.items():
        print("=" * 60)
        print(team)
        print(data)