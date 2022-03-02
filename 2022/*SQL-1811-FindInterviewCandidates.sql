# Write your MySQL query statement below
SELECT DISTINCT t.name, u.mail
FROM (
    SELECT user_id, name, contest_id, 
        LEAD(contest_id, 1) OVER (PARTITION BY user_id ORDER BY contest_id ASC) AS next_1, 
        LEAD(contest_id, 2) OVER (PARTITION BY user_id ORDER BY contest_id ASC) AS next_2
    FROM Users AS u
    LEFT JOIN Contests AS c
    ON u.user_id = c.gold_medal
        OR u.user_id = c.silver_medal
        OR u.user_id = c.bronze_medal
) AS t
LEFT JOIN Users AS u
ON t.user_id = u.user_id
WHERE contest_id + 1 = next_1 AND next_1 + 1 = next_2
UNION
SELECT DISTINCT name, mail
FROM Users
WHERE user_id IN (
    SELECT gold_medal FROM Contests 
    GROUP BY gold_medal HAVING COUNT(gold_medal) >= 3
)