SELECT grouper AS id, COUNT(*) AS num
FROM (
    SELECT requester_id AS grouper, accepter_id AS counter
    FROM RequestAccepted
    UNION ALL 
    SELECT accepter_id AS grouper, requester_id AS counter
    FROM RequestAccepted
) AS t
GROUP BY 1
ORDER BY num DESC
LIMIT 1