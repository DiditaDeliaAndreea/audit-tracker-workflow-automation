"""
Maps operational teams to the worksheet name
within the audit tracker workbook.
"""

TEAM_MAPPING = {
    "Trust & Safety": "Trust & Safety",
    "Moderation": "Moderation",
    "Engineering": "Engineering",
    "Billing": "Billing",
}


def get_sheet_name(team: str) -> str:
    """
    Returns the worksheet name for a team.
    """

    return TEAM_MAPPING.get(team, "Unassigned")