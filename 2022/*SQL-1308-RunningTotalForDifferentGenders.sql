SELECT DISTINCT gender, day, 
    SUM(score_points) OVER (
        PARTITION BY gender ORDER BY day ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS total
FROM Scores
ORDER BY gender ASC, day ASC