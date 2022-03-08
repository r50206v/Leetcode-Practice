SELECT t1.employee_id
FROM (
    SELECT e.employee_id
    FROM Employees AS e
    LEFT JOIN Salaries AS s
    ON e.employee_id = s.employee_id
    WHERE s.salary IS NULL
) AS t1
UNION
SELECT t2.employee_id
FROM (
    SELECT s.employee_id
    FROM Salaries AS s
    LEFT JOIN Employees AS e
    ON e.employee_id = s.employee_id
    WHERE e.name IS NULL
) AS t2
ORDER BY 1