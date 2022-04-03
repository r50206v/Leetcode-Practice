WITH cte AS (
    SELECT student_id, MAX(grade) AS max_grade
    FROM Enrollments
    GROUP BY student_id
)

SELECT e.student_id, MIN(e.course_id) AS course_id, e.grade
FROM cte
LEFT JOIN Enrollments AS e
ON e.student_id = cte.student_id 
    AND e.grade = cte.max_grade
GROUP BY e.student_id, e.grade
ORDER BY e.student_id ASC;