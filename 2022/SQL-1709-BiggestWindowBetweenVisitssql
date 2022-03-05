SELECT user_id, MAX(windows) AS biggest_window
FROM (
    SELECT user_id, DATEDIFF(COALESCE(LEAD(visit_date) OVER (PARTITION BY user_id ORDER BY visit_date), '2021-01-01'), visit_date) AS windows
    FROM UserVisits
) AS t
GROUP BY user_id
ORDER BY user_id