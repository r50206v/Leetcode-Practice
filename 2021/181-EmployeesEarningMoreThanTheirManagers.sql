# Write your MySQL query statement below
SELECT a.Name AS Employee
FROM Employee AS a
LEFT JOIN Employee AS b
ON a.ManagerId = b.Id
WHERE a.Salary > b.Salary;