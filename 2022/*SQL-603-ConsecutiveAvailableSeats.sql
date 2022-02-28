SELECT seat_id
FROM (
    SELECT *, 
        SUM(free) OVER (ORDER BY seat_id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) AS case_1, 
        SUM(free) OVER (ORDER BY seat_id ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS case_2
    FROM Cinema
) AS t
WHERE case_1 >= 2 OR case_2 >=2
ORDER BY seat_id ASC