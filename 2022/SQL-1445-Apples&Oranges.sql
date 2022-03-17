SELECT sale_date, apples - oranges AS diff
FROM (
    SELECT sale_date, 
        SUM(CASE WHEN fruit = 'apples' THEN sold_num ELSE 0 END) AS apples,
        SUM(CASE WHEN fruit = 'oranges' THEN sold_num ELSE 0 END) AS oranges
    FROM Sales
    GROUP BY sale_date
) AS t
ORDER BY sale_date