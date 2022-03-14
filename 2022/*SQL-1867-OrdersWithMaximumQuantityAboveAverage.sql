WITH cte AS (
    SELECT order_id, AVG(quantity) AS avg_q
    FROM OrdersDetails 
    GROUP BY order_id
)


SELECT order_id
FROM (
    SELECT order_id, MAX(quantity) AS max_q
    FROM OrdersDetails
    GROUP BY order_id
) AS a
WHERE a.max_q > (SELECT MAX(avg_q) FROM cte)