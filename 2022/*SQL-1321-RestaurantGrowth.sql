WITH cte AS (
    SELECT visited_on, SUM(amount) AS day_amount
    FROM Customer
    GROUP BY visited_on
)

SELECT visited_on, amount, ROUND(average_amount, 2) AS average_amount
FROM (
    SELECT visited_on, 
    SUM(day_amount) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount, 
    AVG(day_amount) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS average_amount,
    COUNT(day_amount) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS count_days
    FROM cte
) AS t
WHERE count_days = 7