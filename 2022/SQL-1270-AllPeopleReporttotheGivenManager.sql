SELECT employee_id
FROM (
    SELECT a.employee_id, a.manager_id AS m1, b.manager_id AS m2, c.manager_id AS m3
    FROM Employees AS a
    LEFT JOIN Employees AS b
    ON a.manager_id = b.employee_id
    LEFT JOIN Employees AS c
    ON b.manager_id = c.employee_id
) AS t
WHERE (m1 = 1 OR m2 = 1 OR m3 = 1)
    AND employee_id != 1