SELECT
    report_id,
    issue_id,
    reported_at,
    reported_by,
    issue_type,
    severity,
    status,
    assigned_team
FROM user_reports
WHERE status = 'Open'
  AND severity IN ('High', 'Medium')
ORDER BY
    assigned_team,
    reported_at;