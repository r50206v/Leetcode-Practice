SELECT b.project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Employee AS a
LEFT JOIN Project AS b
ON a.employee_id = b.employee_id
WHERE b.project_id IS NOT NULL
GROUP BY 1;