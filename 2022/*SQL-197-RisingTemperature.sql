SELECT id
FROM (
    SELECT id, recordDate, temperature, 
    LAG(temperature) OVER (ORDER BY recordDate) AS previous_temp, 
    LAG(recordDate) OVER (ORDER BY recordDate) prev_date
    FROM Weather
) AS t
WHERE temperature > previous_temp
    AND DATEDIFF(recordDate, prev_date) = 1