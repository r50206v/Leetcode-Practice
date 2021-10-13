CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
Set N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT a.Salary AS getNthHighestSalary
      FROM (
         SELECT DISTINCT Salary
         FROM Employee
         ORDER BY Salary DESC
         LIMIT 1
         OFFSET N
     ) AS a
  );
END