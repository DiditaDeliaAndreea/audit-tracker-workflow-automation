"""
Maps operational teams to their corresponding audit tracker names.
"""

TEAM_MAPPING = {
    "Trust & Safety": "Trust & Safety",
    "Moderation": "Moderation",
    "Engineering": "Engineering",
    "Billing": "Billing"
}


def get_tracker_name(team: str) -> str:
    """
    Returns the audit tracker associated with a team.

    Args:
        team: Name of the operational team.

    Returns:
        Tracker name used for exporting reports.
    """
    return TEAM_MAPPING.get(team, "Unassigned Tracker")