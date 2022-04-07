WITH cte AS (
    SELECT project_id, COUNT(employee_id) AS count_employee
    FROM Project
    GROUP BY project_id
)

SELECT project_id
FROM (
    SELECT project_id, 
        RANK() OVER (ORDER BY count_employee DESC) AS ranking
    FROM cte
) AS t
WHERE ranking = 1;