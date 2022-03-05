SELECT b.book_id, b.name
FROM Books AS b
LEFT JOIN (
    SELECT * FROM Orders
    WHERE dispatch_date > "2018-06-23"
) AS o
ON o.book_id = b.book_id
WHERE DATEDIFF("2019-06-23", b.available_from) > 30
GROUP BY book_id
HAVING SUM(COALESCE(quantity, 0)) < 10