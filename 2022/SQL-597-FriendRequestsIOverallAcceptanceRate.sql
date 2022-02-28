SELECT COALESCE(ROUND(SUM(accepted) / (SELECT COUNT(DISTINCT sender_id, send_to_id) FROM FriendRequest), 2), 0) AS accept_rate
FROM (
    SELECT DISTINCT a.requester_id, a.accepter_id, CASE WHEN a.accept_date IS NULL THEN 0 ELSE 1 END AS accepted
    FROM RequestAccepted AS a
    LEFT JOIN FriendRequest AS b
    ON a.requester_id = b.sender_id
        AND a.accepter_id = b.send_to_id
) AS t