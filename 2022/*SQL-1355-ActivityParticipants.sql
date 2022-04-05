WITH activity_rank AS (
    SELECT activity, 
        RANK() OVER (ORDER BY cp DESC) AS max_ranking, 
        RANK() OVER (ORDER BY cp ASC) AS min_ranking
    FROM (
        SELECT activity, COUNT(*) AS cp
        FROM Friends
        GROUP BY activity
    ) AS t
)

SELECT activity
FROM activity_rank
WHERE max_ranking > 1
    AND min_ranking > 1