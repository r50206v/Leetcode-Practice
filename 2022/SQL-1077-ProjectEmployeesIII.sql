SELECT project_id, employee_id
FROM (
    SELECT p.project_id, p.employee_id,
        RANK() OVER (PARTITION BY p.project_id ORDER BY e.experience_years DESC) AS ranking
    FROM Project AS p
    LEFT JOIN Employee AS e
    ON p.employee_id = e.employee_id
) AS t
WHERE ranking = 1