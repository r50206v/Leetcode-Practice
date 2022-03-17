WITH cte AS (
    SELECT a.machine_id, a.process_id, a.timestamp AS start_time, b.timestamp AS end_time
    FROM Activity AS a
    LEFT JOIN Activity AS b
    ON a.machine_id = b.machine_id 
        AND a.process_id = b.process_id
    WHERE a.activity_type = 'start'
        AND b.activity_type = 'end'
)

SELECT machine_id, ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM cte
GROUP BY machine_id