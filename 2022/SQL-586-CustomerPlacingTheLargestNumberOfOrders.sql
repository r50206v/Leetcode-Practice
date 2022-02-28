SELECT customer_number
FROM (
    SELECT customer_number, COUNT(*) AS count_order
    FROM Orders
    GROUP BY customer_number
    ORDER BY count_order DESC
    LIMIT 1
) AS t