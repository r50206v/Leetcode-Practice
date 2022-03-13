WITH Fri AS (
    SELECT user1_id as id1, user2_id as id2 FROM Friendship
    UNION 
    SELECT user2_id as id1, user1_id as id2 FROM Friendship
)

SELECT f1.id1 as user1_id, f1.id2 as user2_id, COUNT(*) as common_friend 
FROM Fri AS f1
JOIN Fri AS f2 ON f1.id1=f2.id1 AND f1.id2<>f2.id2
JOIN Fri AS f3 ON f1.id2=f3.id1 AND f2.id2=f3.id2
WHERE f1.id1 < f1.id2
GROUP BY f1.id1, f1.id2
HAVING COUNT(*) >=3