from pathlib import Path
import html
import sqlite3


BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_PATH = BASE_DIR / "database" / "connecthub_demo.db"
BUG_REPORTS_DIR = BASE_DIR / "bug_reports"


BUG_DETAILS = {
    "Spam Account": {
        "description": (
            "A blocked account continues sending unsolicited messages after "
            "the user completes the block and report flow."
        ),
        "platform": "Web",
        "operating_system": "Windows 11",
        "browser": "Chrome 126",
        "steps": [
            "Sign in to the social application.",
            "Open the Messages section.",
            "Open a conversation with the reported account.",
            "Select Block and Report.",
            "Refresh the page.",
            "Return to the Messages section.",
        ],
        "expected": (
            "The blocked account should no longer be able to send messages "
            "or appear in the user's active conversations."
        ),
        "actual": (
            "New messages from the blocked account continue to appear after "
            "the page is refreshed."
        ),
        "severity": "Major",
        "priority": "High",
        "evidence": "Screenshot showing a new message received after blocking.",
        "source_url": "https://connecthub.example/messages",
        "reported_by": "Demo QA Analyst",
        "assigned_to": "Trust & Safety Team",
    },
    "Offensive Content": {
        "description": (
            "Reported offensive content remains visible in the user's feed "
            "after a successful report submission."
        ),
        "platform": "Mobile",
        "operating_system": "iOS 18",
        "browser": "ConnectHub iOS App",
        "steps": [
            "Open the social application.",
            "Navigate to the affected post.",
            "Select Report.",
            "Choose Offensive Content.",
            "Submit the report.",
            "Refresh the feed.",
        ],
        "expected": (
            "The reported content should be hidden from the reporting user's feed."
        ),
        "actual": (
            "The reported post remains visible after the report is submitted."
        ),
        "severity": "Major",
        "priority": "High",
        "evidence": "Screen recording showing the completed report flow.",
        "source_url": "https://connecthub.example/feed",
        "reported_by": "Demo QA Analyst",
        "assigned_to": "Moderation Team",
    },
    "Payment Failure": {
        "description": (
            "The application shows a payment failure message even though the "
            "payment provider confirms that the transaction completed."
        ),
        "platform": "Web",
        "operating_system": "macOS 15",
        "browser": "Safari 18",
        "steps": [
            "Sign in to the application.",
            "Open the subscription page.",
            "Select a paid plan.",
            "Enter valid payment details.",
            "Submit the payment.",
        ],
        "expected": (
            "The payment should complete and the account should be upgraded."
        ),
        "actual": (
            "An error message appears and the subscription remains inactive."
        ),
        "severity": "Critical",
        "priority": "High",
        "evidence": (
            "Screenshot of the application error and payment provider confirmation."
        ),
        "source_url": "https://connecthub.example/subscription",
        "reported_by": "Demo QA Analyst",
        "assigned_to": "Billing Team",
    },
    "Harassment Report": {
        "description": (
            "The application does not display confirmation after a user "
            "submits a harassment report."
        ),
        "platform": "Mobile",
        "operating_system": "Android 15",
        "browser": "ConnectHub Android App",
        "steps": [
            "Open the application.",
            "Navigate to a user profile.",
            "Select Report User.",
            "Choose Harassment.",
            "Add report details.",
            "Submit the report.",
        ],
        "expected": (
            "A confirmation message should indicate that the report was submitted."
        ),
        "actual": (
            "The dialog closes without confirmation."
        ),
        "severity": "Minor",
        "priority": "Medium",
        "evidence": "Video recording of the report submission flow.",
        "source_url": "https://connecthub.example/profile",
        "reported_by": "Demo QA Analyst",
        "assigned_to": "Moderation Team",
    },
    "Fake Giveaway": {
        "description": (
            "A reported scam giveaway remains visible in search after being "
            "flagged by multiple users."
        ),
        "platform": "Web",
        "operating_system": "Windows 11",
        "browser": "Edge 126",
        "steps": [
            "Sign in to the application.",
            "Search for the giveaway post.",
            "Open the post.",
            "Submit a Scam report.",
            "Return to search.",
            "Search for the same post again.",
        ],
        "expected": (
            "The reported post should be hidden from the reporting user's results."
        ),
        "actual": (
            "The reported post remains visible and accessible."
        ),
        "severity": "Major",
        "priority": "High",
        "evidence": "Screenshots taken before and after submitting the report.",
        "source_url": "https://connecthub.example/search",
        "reported_by": "Demo QA Analyst",
        "assigned_to": "Trust & Safety Team",
    },
    "Impersonation": {
        "description": (
            "The impersonation report form allows submission without the "
            "required supporting evidence."
        ),
        "platform": "Web",
        "operating_system": "Windows 11",
        "browser": "Firefox 128",
        "steps": [
            "Open the reported profile.",
            "Select Report User.",
            "Choose Impersonation.",
            "Leave the evidence field empty.",
            "Submit the report.",
        ],
        "expected": (
            "The form should require supporting evidence before submission."
        ),
        "actual": (
            "The report is submitted successfully with no evidence attached."
        ),
        "severity": "Minor",
        "priority": "Medium",
        "evidence": "Screenshot of the successful submission with no evidence.",
        "source_url": "https://connecthub.example/report",
        "reported_by": "Demo QA Analyst",
        "assigned_to": "Moderation Team",
    },
}


DEFAULT_BUG = {
    "description": "A functional issue was reported in the social application.",
    "platform": "Web",
    "operating_system": "Windows 11",
    "browser": "Chrome 126",
    "steps": [
        "Open the application.",
        "Navigate to the affected feature.",
        "Perform the reported action.",
        "Observe the result.",
    ],
    "expected": "The feature should complete successfully.",
    "actual": "The feature does not behave as expected.",
    "severity": "Major",
    "priority": "Medium",
    "evidence": "Screenshot or video showing the issue.",
    "source_url": "https://connecthub.example",
    "reported_by": "Demo QA Analyst",
    "assigned_to": "Engineering Team",
}


def severity_class(severity: str) -> str:
    """Return the CSS class associated with a severity level."""
    return {
        "Critical": "critical",
        "Major": "major",
        "Minor": "minor",
        "Trivial": "trivial",
    }.get(severity, "minor")


def status_class(status: str) -> str:
    """Return the CSS class associated with a status."""
    normalized_status = status.strip().lower()

    return {
        "open": "status-open",
        "new": "status-open",
        "in progress": "status-progress",
        "resolved": "status-resolved",
        "closed": "status-resolved",
    }.get(normalized_status, "status-open")


def create_steps_html(steps: list[str]) -> str:
    """Convert reproduction steps into an ordered HTML list."""
    items = "".join(
        f"<li>{html.escape(step)}</li>"
        for step in steps
    )
    return f"<ol>{items}</ol>"


def generate_bug_reports() -> int:
    """Create one local HTML QA bug report for each database issue."""

    if not DATABASE_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DATABASE_PATH}"
        )

    BUG_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as connection:
        rows = connection.execute(
            """
            SELECT
                issue_id,
                created_date,
                team,
                area,
                title,
                tags,
                status
            FROM user_reports
            ORDER BY created_date
            """
        ).fetchall()

    for issue_id, created_date, team, area, title, tags, status in rows:
        details = BUG_DETAILS.get(title, DEFAULT_BUG)

        safe_issue_id = html.escape(issue_id)
        safe_created_date = html.escape(created_date)
        safe_team = html.escape(team)
        safe_area = html.escape(area)
        safe_title = html.escape(title)
        safe_tags = html.escape(tags)
        safe_status = html.escape(status)

        report_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{safe_issue_id} - {safe_title}</title>

    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            padding: 36px 20px;
            background: #f3f4f6;
            color: #1f2937;
            font-family: Arial, Helvetica, sans-serif;
        }}

        .page {{
            max-width: 1000px;
            margin: 0 auto;
        }}

        .top-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            padding: 14px 20px;
            background: #172554;
            color: white;
            border-radius: 10px 10px 0 0;
        }}

        .product-name {{
            font-size: 15px;
            font-weight: 700;
            letter-spacing: 0.4px;
        }}

        .demo-label {{
            font-size: 12px;
            opacity: 0.8;
        }}

        .issue-header {{
            padding: 28px 30px;
            background: white;
            border-left: 1px solid #d1d5db;
            border-right: 1px solid #d1d5db;
        }}

        .issue-key {{
            margin-bottom: 8px;
            color: #2563eb;
            font-size: 14px;
            font-weight: 700;
        }}

        h1 {{
            margin: 0;
            color: #111827;
            font-size: 28px;
            line-height: 1.3;
        }}

        .badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 18px;
        }}

        .badge {{
            display: inline-block;
            padding: 6px 11px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
        }}

        .status-open {{
            background: #dbeafe;
            color: #1d4ed8;
        }}

        .status-progress {{
            background: #fef3c7;
            color: #92400e;
        }}

        .status-resolved {{
            background: #dcfce7;
            color: #166534;
        }}

        .critical {{
            background: #fee2e2;
            color: #991b1b;
        }}

        .major {{
            background: #ffedd5;
            color: #9a3412;
        }}

        .minor {{
            background: #fef3c7;
            color: #854d0e;
        }}

        .trivial {{
            background: #e5e7eb;
            color: #374151;
        }}

        .priority {{
            background: #ede9fe;
            color: #6d28d9;
        }}

        .content {{
            display: grid;
            grid-template-columns: minmax(0, 2fr) minmax(260px, 1fr);
            gap: 22px;
            padding: 24px;
            background: #f8fafc;
            border: 1px solid #d1d5db;
            border-top: none;
            border-radius: 0 0 10px 10px;
        }}

        .main-column,
        .side-column {{
            display: flex;
            flex-direction: column;
            gap: 18px;
        }}

        .card {{
            padding: 22px;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
        }}

        .card h2 {{
            margin: 0 0 14px;
            padding-bottom: 9px;
            border-bottom: 2px solid #dbeafe;
            color: #1e3a8a;
            font-size: 17px;
        }}

        .card p {{
            margin: 0;
            line-height: 1.65;
        }}

        .detail-row {{
            margin-bottom: 14px;
        }}

        .detail-row:last-child {{
            margin-bottom: 0;
        }}

        .label {{
            display: block;
            margin-bottom: 4px;
            color: #6b7280;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.4px;
            text-transform: uppercase;
        }}

        .value {{
            color: #111827;
            font-size: 14px;
            line-height: 1.5;
        }}

        ol {{
            margin: 0;
            padding-left: 22px;
            line-height: 1.75;
        }}

        a {{
            color: #2563eb;
            word-break: break-all;
        }}

        .evidence-box {{
            padding: 14px;
            background: #f9fafb;
            border: 1px dashed #9ca3af;
            border-radius: 6px;
        }}

        .footer-note {{
            margin-top: 16px;
            color: #6b7280;
            font-size: 12px;
            text-align: center;
        }}

        @media (max-width: 760px) {{
            .content {{
                grid-template-columns: 1fr;
            }}

            .top-bar {{
                align-items: flex-start;
                flex-direction: column;
            }}

            h1 {{
                font-size: 23px;
            }}
        }}
    </style>
</head>

<body>
    <div class="page">
        <div class="top-bar">
            <div class="product-name">ConnectHub Bug Tracking</div>
            <div class="demo-label">Public portfolio demonstration</div>
        </div>

        <section class="issue-header">
            <div class="issue-key">{safe_issue_id}</div>
            <h1>{safe_title}</h1>

            <div class="badges">
                <span class="badge {status_class(status)}">
                    {safe_status}
                </span>

                <span class="badge {severity_class(details["severity"])}">
                    Severity: {html.escape(details["severity"])}
                </span>

                <span class="badge priority">
                    Priority: {html.escape(details["priority"])}
                </span>
            </div>
        </section>

        <main class="content">
            <div class="main-column">
                <section class="card">
                    <h2>Description</h2>
                    <p>{html.escape(details["description"])}</p>
                </section>

                <section class="card">
                    <h2>Steps to Reproduce</h2>
                    {create_steps_html(details["steps"])}
                </section>

                <section class="card">
                    <h2>Expected Result</h2>
                    <p>{html.escape(details["expected"])}</p>
                </section>

                <section class="card">
                    <h2>Actual Result</h2>
                    <p>{html.escape(details["actual"])}</p>
                </section>

                <section class="card">
                    <h2>Evidence</h2>
                    <div class="evidence-box">
                        {html.escape(details["evidence"])}
                    </div>
                </section>
            </div>

            <aside class="side-column">
                <section class="card">
                    <h2>Issue Details</h2>

                    <div class="detail-row">
                        <span class="label">Bug ID</span>
                        <div class="value">{safe_issue_id}</div>
                    </div>

                    <div class="detail-row">
                        <span class="label">Reported By</span>
                        <div class="value">
                            {html.escape(details["reported_by"])}
                        </div>
                    </div>

                    <div class="detail-row">
                        <span class="label">Date Reported</span>
                        <div class="value">{safe_created_date}</div>
                    </div>

                    <div class="detail-row">
                        <span class="label">Assigned To</span>
                        <div class="value">
                            {html.escape(details["assigned_to"])}
                        </div>
                    </div>

                    <div class="detail-row">
                        <span class="label">Team</span>
                        <div class="value">{safe_team}</div>
                    </div>

                    <div class="detail-row">
                        <span class="label">Area</span>
                        <div class="value">{safe_area}</div>
                    </div>

                    <div class="detail-row">
                        <span class="label">Tags</span>
                        <div class="value">{safe_tags}</div>
                    </div>
                </section>

                <section class="card">
                    <h2>Environment</h2>

                    <div class="detail-row">
                        <span class="label">Platform</span>
                        <div class="value">
                            {html.escape(details["platform"])}
                        </div>
                    </div>

                    <div class="detail-row">
                        <span class="label">Operating System</span>
                        <div class="value">
                            {html.escape(details["operating_system"])}
                        </div>
                    </div>

                    <div class="detail-row">
                        <span class="label">Browser / App</span>
                        <div class="value">
                            {html.escape(details["browser"])}
                        </div>
                    </div>
                </section>

                <section class="card">
                    <h2>Source URL</h2>
                    <a
                        href="{html.escape(details["source_url"])}"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        {html.escape(details["source_url"])}
                    </a>
                </section>
            </aside>
        </main>

        <div class="footer-note">
            Fictional report generated for the Audit Tracker Workflow Automation portfolio.
        </div>
    </div>
</body>
</html>
"""

        output_file = BUG_REPORTS_DIR / f"{issue_id}.html"
        output_file.write_text(report_html, encoding="utf-8")

    return len(rows)


if __name__ == "__main__":
    created_count = generate_bug_reports()
    print(f"QA bug reports created: {created_count}")
    print(f"Output directory: {BUG_REPORTS_DIR}")