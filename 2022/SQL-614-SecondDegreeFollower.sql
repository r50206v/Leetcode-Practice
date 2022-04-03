SELECT a.follower, COUNT(DISTINCT b.follower) AS num
FROM Follow AS a
LEFT JOIN Follow AS b
ON a.follower = b.followee
WHERE b.follower IS NOT NULL
GROUP BY a.follower
ORDER BY a.follower ASC