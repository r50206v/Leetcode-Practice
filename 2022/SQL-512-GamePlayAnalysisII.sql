# Write your MySQL query statement below
SELECT t1.player_id, t2.device_id
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) AS t1
LEFT JOIN Activity AS t2
ON t1.player_id = t2.player_id 
    AND t1.first_login = t2.event_date