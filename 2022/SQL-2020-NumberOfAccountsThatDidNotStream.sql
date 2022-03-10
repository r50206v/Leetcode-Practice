SELECT COUNT(DISTINCT(account_id)) AS accounts_count
FROM (
        SELECT a.account_id, b.stream_date, CASE WHEN '2021-01-01' BETWEEN a.start_date AND a.end_date THEN 1 ELSE 0 END AS sub_2021
    FROM Subscriptions AS a
    LEFT JOIN Streams AS b
    ON a.account_id = b.account_id
) AS t
WHERE sub_2021 = 1
    AND stream_date NOT BETWEEN '2021-01-01' AND '2021-12-31';