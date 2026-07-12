# Audit Tracker Workflow Automation

## Overview

This repository demonstrates a production-inspired Python automation that prepares weekly audit trackers by automatically extracting operational reports, applying business rules, routing reports to the correct audit team and updating a multi-sheet audit tracker.

The original solution was implemented as a scheduled Python notebook within an internal environment. This public version recreates the engineering workflow using SQLite, SQL, Pandas and Excel while excluding all proprietary systems, confidential data and internal business logic.

---

## Business Problem

The audit preparation process was previously performed manually every week.

The workflow required analysts to:

- Open the operational dashboard
- Apply business filters
- Review eligible issue reports
- Copy issue identifiers
- Paste reports into the correct audit tracker
- Repeat the process for each operational team
- Prevent duplicate audit entries manually

The process was repetitive, time-consuming and susceptible to copy-and-paste errors.

---

## Solution

The automation performs the complete workflow automatically.

### Workflow

1. Execute the scheduled workflow
2. Query the operational data source
3. Apply SQL business rules
4. Extract eligible issue reports
5. Group reports by operational team
6. Prepare tracker-ready datasets
7. Generate clickable issue report hyperlinks
8. Read existing tracker entries
9. Detect previously exported issues
10. Insert only new reports
11. Update the appropriate team worksheet
12. Produce an execution summary

---

# Workflow Architecture

![Workflow Architecture](docs/images/workflow-architecture.png)

---

# Manual vs Automated Process

![Before vs After](docs/images/before-after.png)

---

# Repository Structure

```text
audit-tracker-workflow-automation/
│
├── demo/
│   ├── bug_reports/
│   │   ├── ISSUE-xxxxx.html
│   │   └── ...
│   │
│   ├── database/
│   │   ├── connecthub_demo.db
│   │   ├── create_database.py
│   │   └── generate_bug_reports.py
│   │
│   ├── output/
│   │   └── audit_tracker_demo.xlsx
│   │
│   ├── scheduler/
│   │   └── schedule.md
│   │
│   ├── sql/
│   │   └── filter_reports.sql
│   │
│   └── src/
│       ├── deduplicate_reports.py
│       ├── excel_tracker.py
│       ├── extract_reports.py
│       ├── group_by_team.py
│       ├── prepare_tracker_data.py
│       ├── run_workflow.py
│       └── team_mapping.py
│
├── docs/
│   └── images/
│
└── README.md
```

---

# Demo Workflow

```
                 Scheduled Workflow
                        │
                        ▼
              SQLite Demo Database
                        │
                        ▼
              SQL Business Filtering
                        │
                        ▼
                 Extract Reports
                        │
                        ▼
                 Group by Team
                        │
                        ▼
            Prepare Tracker Dataset
                        │
                        ▼
            Open Audit Tracker Workbook
                        │
                        ▼
          Read Existing Tracker Entries
                        │
                        ▼
             Remove Duplicate Reports
                        │
                        ▼
      Generate Clickable Issue Reports
                        │
                        ▼
         Update Team Worksheets in Excel
                        │
                        ▼
               Processing Summary
```

---

# Scheduling

In production, the workflow was configured using the notebook platform's built-in scheduler.

**Schedule**

- Frequency: Weekly
- Day: Monday
- Time: 12:00 PM
- Time Zone: Europe/Dublin

The SQL query retrieves reports created during the previous Monday–Sunday reporting period regardless of the execution date.

For this public demonstration, the workflow is executed manually:

```bash
python demo/src/run_workflow.py
```

---

# Technologies

- Python
- SQL
- SQLite
- Pandas
- OpenPyXL
- HTML
- VS Code

---

# Features

- SQL business rule filtering
- Dynamic weekly reporting period
- Team-based routing
- Multi-sheet audit tracker
- Automatic worksheet creation
- Clickable issue report pages
- Duplicate detection
- Incremental tracker updates
- Processing summary
- Modular architecture

---

# Engineering Decisions

The project follows a modular architecture where each module has a single responsibility.

| Module | Responsibility |
|----------|----------------|
| `extract_reports.py` | Executes SQL queries and retrieves reports |
| `group_by_team.py` | Groups reports by operational team |
| `prepare_tracker_data.py` | Builds tracker-ready datasets |
| `team_mapping.py` | Maps teams to Excel worksheets |
| `deduplicate_reports.py` | Prevents duplicate report exports |
| `excel_tracker.py` | Handles Excel workbook operations |
| `run_workflow.py` | Orchestrates the complete workflow |

---

# Issue Reports

Each exported issue contains a clickable hyperlink that opens a generated issue report.

The reports simulate operational issues submitted by employees through an internal reporting system.

Each report includes:

- Issue ID
- Title
- Description
- Environment
- Steps to Reproduce
- Expected Result
- Actual Result
- Severity
- Priority
- Supporting Evidence
- Source URL
- Reported By
- Assigned Team
- Status

---

# Results

Compared to the manual process, the automation:

- Eliminates repetitive copy-and-paste work
- Applies consistent SQL filtering
- Automatically routes reports to the correct team
- Prevents duplicate exports
- Produces tracker-ready worksheets
- Generates clickable issue reports
- Reduces preparation from a repetitive manual process to a single workflow execution

---

# Skills Demonstrated

- Python Automation
- SQL Development
- Data Processing with Pandas
- Workflow Automation
- Process Improvement
- Software Design
- Data Validation
- Excel Automation
- Technical Documentation

---

# Disclaimer

This repository is a public engineering demonstration inspired by a production workflow.

All report titles, issue identifiers, employee reports, operational teams and business entities are fictional and created solely for demonstration purposes.

No proprietary code, confidential business logic or internal systems are included.