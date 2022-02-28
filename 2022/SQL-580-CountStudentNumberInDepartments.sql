SELECT d.dept_name, COUNT(DISTINCT s.student_id) AS student_number
FROM Department AS d
LEFT JOIN Student AS s
ON d.dept_id = s.dept_id
GROUP BY 1
ORDER BY student_number DESC;