SELECT d.Name AS Department, e.Name AS Employee, e.Salary
FROM (
    SELECT DepartmentId, MAX(Salary) AS MaxSalary
    FROM Employee
    GROUP BY DepartmentId
) AS t
RIGHT JOIN Employee AS e
ON e.DepartmentId = t.DepartmentId
LEFT JOIN Department AS d
ON t.DepartmentId = d.Id
WHERE e.Salary = t.MaxSalary;