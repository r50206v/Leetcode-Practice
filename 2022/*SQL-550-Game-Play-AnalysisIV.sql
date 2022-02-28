SELECT ROUND(COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity AS a
LEFT JOIN (
    SELECT player_id, MIN(event_date) AS first_date 
    FROM Activity 
    GROUP BY player_id
) AS b
ON a.player_id = b.player_id
WHERE DATEDIFF(b.first_date, a.event_date) = -1