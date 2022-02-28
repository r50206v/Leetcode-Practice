SELECT DISTINCT b.name AS Department, a.name AS Employee, a.salary AS Salary
FROM Employee AS a
LEFT JOIN Department AS b
ON a.departmentId = b.id
LEFT JOIN (
    SELECT departmentId, salary, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS `rank`
    FROM Employee
) AS c
ON a.departmentId = c.departmentId
AND a.salary = c.salary
WHERE c.rank <= 3
ORDER BY Department, Salary DESC