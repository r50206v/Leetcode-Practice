WITH cte AS (
    SELECT s.student_id, s.student_name, s.subject_name, 
        COALESCE(COUNT(e.student_id), 0) AS attended_exams
    FROM (SELECT * FROM Subjects, Students) AS s
    LEFT JOIN Examinations AS e
    ON s.subject_name = e.subject_name
        AND e.student_id = s.student_id
    GROUP BY s.student_id, s.subject_name
)


SELECT * FROM cte
ORDER BY student_id, subject_name