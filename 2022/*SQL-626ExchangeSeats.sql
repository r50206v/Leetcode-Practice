SELECT id, 
    CASE WHEN id % 2 = 1 AND odd IS NOT NULL THEN odd 
        WHEN id % 2 = 1 AND odd IS NULL THEN student
        ELSE even END AS student
FROM (
    SELECT id, student,
        LEAD(student) OVER (ORDER BY id) AS odd,
        LAG(student) OVER (ORDER BY id) AS even
    FROM Seat
) AS t