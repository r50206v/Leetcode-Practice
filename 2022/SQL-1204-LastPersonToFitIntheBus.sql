SELECT person_name
FROM (
    SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) <= 1000 AS total_weight
    FROM Queue
) AS t
WHERE total_weight = 1
ORDER BY turn DESC
LIMIT 1;