SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary
FROM Employee AS e
LEFT JOIN (
    SELECT DISTINCT DepartmentId, Salary, DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS `Rank`
    FROM Employee    
) AS f
ON e.DepartmentId = f.DepartmentId
AND e.Salary = f.Salary
LEFT JOIN Department AS d
ON e.DepartmentId = d.Id
WHERE f.Rank <= 3
ORDER BY Department, Salary DESC