WITH reporting_period AS (
    SELECT
        date('now', 'weekday 1', '-14 days') AS week_start,
        date('now', 'weekday 1', '-8 days') AS week_end
)

SELECT
    issue_id,
    created_date,
    team,
    area,
    title,
    tags
FROM user_reports, reporting_period
WHERE
    status <> 'Closed'
    AND team IN (
        'Trust & Safety',
        'Moderation',
        'Engineering',
        'Billing'
    )
    AND area IN (
        'User Reports',
        'Payments',
        'Mobile App',
        'Backend'
    )
    AND tags LIKE '%review%'
    AND date(created_date) BETWEEN week_start AND week_end
ORDER BY
    team,
    created_date;