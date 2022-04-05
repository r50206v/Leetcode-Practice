WITH cte AS (
    SELECT a.x, b.x AS y, ABS(a.x - b.x) AS distance
    FROM Point AS a, Point AS b
    WHERE a.x != b.x
)

SELECT distance AS shortest
FROM cte
ORDER BY distance ASC
LIMIT 1;