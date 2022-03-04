WITH cte AS (
    SELECT DISTINCT id, login_date
    FROM Logins
)

SELECT DISTINCT a.id, a.name
FROM (
    SELECT id, COUNT(*) OVER (PARTITION BY id ORDER BY login_date RANGE INTERVAL '5' DAY PRECEDING) AS 5_days
    FROM cte
) AS t
LEFT JOIN Accounts AS a
ON t.id = a.id
WHERE t.5_days = 5