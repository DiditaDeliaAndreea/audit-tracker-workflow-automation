# Production Schedule

In production, this workflow was configured using the notebook platform's built-in scheduler.

Schedule:

- Frequency: Weekly
- Day: Monday
- Time: 12:00
- Time Zone: Europe/Dublin

The scheduled execution automatically:

1. Runs the SQL extraction.
2. Retrieves reports created during the previous Monday–Sunday period.
3. Applies business rules.
4. Updates the audit tracker.
5. Prevents duplicate exports.
6. Produces a processing summary.

The public version is executed manually by running:

```bash
python demo/src/run_workflow.py
```