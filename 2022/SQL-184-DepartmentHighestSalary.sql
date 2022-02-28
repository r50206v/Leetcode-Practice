SELECT c.name AS Department, a.name AS Employee, a.salary AS Salary
FROM Employee AS a
LEFT JOIN (
    SELECT departmentId, MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentId
) AS b
ON a.departmentId = b.departmentId
LEFT JOIN Department AS c
ON a.departmentId = c.id
WHERE a.salary = b.max_salary;