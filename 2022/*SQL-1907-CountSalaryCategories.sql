WITH cte (category) AS (
    SELECT "Low Salary" FROM DUAL
    UNION 
    SELECT "Average Salary" FROM DUAL
    UNION 
    SELECT "High Salary" FROM DUAL
)



SELECT cte.category, COUNT(DISTINCT t.account_id) AS accounts_count
FROM cte
LEFT JOIN (
    SELECT account_id, income, 
        CASE WHEN income < 20000 THEN "Low Salary"
            WHEN income <= 50000 THEN "Average Salary"
            ELSE "High Salary" END AS category
    FROM Accounts
) AS t
ON cte.category = t.category
GROUP BY 1