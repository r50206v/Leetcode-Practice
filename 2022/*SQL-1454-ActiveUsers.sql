WITH cte AS (
    SELECT DISTINCT id, login_date
    FROM Logins
)

SELECT DISTINCT a.id, a.name
FROM (
    SELECT id, DATEDIFF(LEAD(login_date, 4) OVER (PARTITION BY id ORDER BY login_date), login_date) AS 5_days
    FROM cte
) AS t
LEFT JOIN Accounts AS a
ON t.id = a.id
WHERE t.5_days = 4