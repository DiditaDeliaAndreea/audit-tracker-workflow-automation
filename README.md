# Audit Tracker Workflow Automation

## Overview

This repository demonstrates a production-inspired Python workflow automation that prepares weekly audit trackers by automatically extracting operational reports, applying business rules, preparing tracker-ready datasets and updating team-specific audit worksheets.

The original solution was implemented as a scheduled Python notebook within an internal environment. This public project recreates the engineering workflow using SQLite, SQL, Pandas and Excel while excluding all proprietary code, internal systems and confidential business logic.

---

## Business Problem

The audit preparation process was previously performed manually every week.

The workflow required:

- Extracting operational reports
- Applying business filtering rules
- Separating reports by operational team
- Copying reports into team audit trackers
- Creating report hyperlinks
- Checking for already audited reports
- Preventing duplicate entries
- Preparing trackers before auditors started work

The manual process was repetitive, time-consuming and susceptible to copy-paste errors.

---

## Solution

The automation performs the complete workflow automatically.

### Workflow

1. Execute SQL query against the operational data source
2. Apply business rule filtering
3. Extract eligible reports
4. Group reports by operational team
5. Prepare tracker-ready datasets
6. Generate report hyperlinks
7. Read existing tracker data
8. Detect previously exported reports
9. Insert only new reports
10. Update the appropriate team worksheet
11. Print an execution summary

---

## Workflow Architecture

![Workflow Architecture](docs/images/Workflow-Architecture-(technical).png)

---

## Before vs After

![Before vs After](docs/images/Manual-vs-Automated-Workflow-(business value).png)

---

## Repository Structure

```text
demo/
│
├── database/
│   ├── create_database.py
│   └── connecthub_demo.db
│
├── output/
│   └── audit_tracker_demo.xlsx
│
├── sql/
│   └── filter_reports.sql
│
└── src/
    ├── deduplicate_reports.py
    ├── excel_tracker.py
    ├── extract_reports.py
    ├── group_by_team.py
    ├── prepare_tracker_data.py
    ├── run_workflow.py
    └── team_mapping.py
```

---

## Project Workflow

```
SQLite Database
        │
        ▼
SQL Filtering
        │
        ▼
Extract Reports
        │
        ▼
Group by Team
        │
        ▼
Prepare Tracker Data
        │
        ▼
Open Audit Tracker
        │
        ▼
Read Existing Reports
        │
        ▼
Remove Duplicates
        │
        ▼
Update Team Worksheet
        │
        ▼
Processing Summary
```

---

## Technologies

- Python
- SQL
- SQLite
- Pandas
- OpenPyXL
- VS Code

---

## Features

- Automated SQL data extraction
- Business rule filtering
- Team-based report routing
- Dynamic report hyperlink generation
- Duplicate detection
- Multi-sheet audit tracker updates
- Automatic worksheet creation
- Header management
- Processing summary
- Modular architecture

---

## Engineering Decisions

This project follows a modular architecture where each module has a single responsibility.

| Module | Responsibility |
|---------|----------------|
| extract_reports.py | Executes SQL and retrieves reports |
| group_by_team.py | Splits reports by operational team |
| prepare_tracker_data.py | Builds tracker-ready datasets |
| team_mapping.py | Maps teams to tracker worksheets |
| deduplicate_reports.py | Prevents duplicate report exports |
| excel_tracker.py | Handles Excel workbook operations |
| run_workflow.py | Orchestrates the complete automation |

---

## Example Output

The automation updates a multi-sheet audit tracker.

Each worksheet represents one operational team.

Example worksheets:

- Trust & Safety
- Moderation
- Engineering
- Billing

Only reports that have not been previously exported are inserted.

New reports are always added at the top of the worksheet.

---

## Results

Compared to the manual process, the automation:

- Eliminated manual copy-and-paste work
- Prevented duplicate report exports
- Applied consistent business filtering
- Automatically routed reports to the correct team worksheet
- Reduced preparation time from a manual task to a single workflow execution
- Produced audit trackers ready for review before auditors started work

---

## Skills Demonstrated

- Python Automation
- SQL Development
- Data Processing with Pandas
- Workflow Automation
- Process Improvement
- Data Validation
- Duplicate Detection
- Software Architecture
- Technical Documentation

---

## Disclaimer

This repository is a public engineering demonstration inspired by a production workflow.

All report titles, issue identifiers, operational teams and business entities are fictional.

No proprietary code, confidential business logic or internal systems are included.
