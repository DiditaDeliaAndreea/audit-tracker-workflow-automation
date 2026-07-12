from deduplicate_reports import remove_existing_reports
from excel_tracker import (
    ensure_headers,
    get_existing_issue_numbers,
    get_or_create_sheet,
    insert_dataframe_at_top,
    open_tracker,
    save_tracker,
)
from extract_reports import extract_reports
from group_by_team import group_by_team
from prepare_tracker_data import prepare_tracker_data
from team_mapping import get_sheet_name


def run_workflow() -> None:
    """Run the complete audit tracker automation workflow."""

    reports_df = extract_reports()
    grouped_reports = group_by_team(reports_df)

    workbook = open_tracker()

    total_inserted = 0
    summary = {}

    for team, team_df in grouped_reports.items():
        sheet_name = get_sheet_name(team)

        prepared_df = prepare_tracker_data(team_df)

        worksheet = get_or_create_sheet(
            workbook,
            sheet_name,
        )

        ensure_headers(
            worksheet,
            prepared_df.columns.tolist(),
        )

        existing_issue_numbers = get_existing_issue_numbers(
            worksheet
        )

        new_reports_df = remove_existing_reports(
            prepared_df,
            existing_issue_numbers,
        )

        inserted_count = insert_dataframe_at_top(
            worksheet,
            new_reports_df,
        )

        summary[team] = {
            "retrieved": len(team_df),
            "existing": len(prepared_df) - len(new_reports_df),
            "inserted": inserted_count,
        }

        total_inserted += inserted_count

    save_tracker(workbook)

    print("\n" + "=" * 60)
    print("AUDIT TRACKER WORKFLOW COMPLETED")
    print("=" * 60)
    print(f"Filtered reports retrieved: {len(reports_df)}")
    print(f"New reports inserted: {total_inserted}")
    print()

    for team, result in summary.items():
        print(
            f"{team}: "
            f"{result['retrieved']} retrieved, "
            f"{result['existing']} already present, "
            f"{result['inserted']} inserted"
        )

    print("=" * 60)


if __name__ == "__main__":
    run_workflow()