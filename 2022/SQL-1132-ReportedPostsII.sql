SELECT ROUND(AVG(pct_remove) * 100, 2) AS average_daily_percent
FROM (
    SELECT a.action_date, COUNT(DISTINCT r.post_id) / COUNT(DISTINCT a.post_id) AS pct_remove
    FROM Actions AS a
    LEFT JOIN Removals AS r
    ON a.post_id = r.post_id
    WHERE a.extra = 'spam'
    GROUP BY a.action_date
) AS t