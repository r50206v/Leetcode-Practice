SELECT e1.employee_id, e2.name, e1.reports_count, e1.average_age
FROM (
    SELECT reports_to AS employee_id, COUNT(employee_id) AS reports_count, 
        ROUND(AVG(age), 0) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
) AS e1
LEFT JOIN Employees AS e2
ON e1.employee_id = e2.employee_id
ORDER BY employee_id ASC