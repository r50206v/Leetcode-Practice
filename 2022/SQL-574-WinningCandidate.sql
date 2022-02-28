SELECT t.name
FROM (
    SELECT b.name, COUNT(*) AS vote_count
    FROM Vote AS a
    LEFT JOIN Candidate AS b
    ON a.candidateId = b.id
    GROUP BY 1
) AS t
ORDER BY vote_count DESC 
LIMIT 1;