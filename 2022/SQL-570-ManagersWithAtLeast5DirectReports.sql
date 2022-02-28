SELECT a.name
FROM Employee AS a
LEFT JOIN (
    SELECT managerId, COUNT(DISTINCT id) AS direct_report
    FROM Employee
    GROUP BY managerId
) AS b
ON a.id = b.managerId
WHERE b.direct_report >= 5