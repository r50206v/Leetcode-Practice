WITH cte AS (
    SELECT c.customer_id, c.name, MONTH(o.order_date) AS month, SUM(p.price * o.quantity) AS monthly_purchase
    FROM Orders AS o
    LEFT JOIN Customers AS c
    ON o.customer_id = c.customer_id
    LEFT JOIN Product AS p
    ON o.product_id = p.product_id
    WHERE MONTH(o.order_date) IN (6,7)
        AND YEAR(o.order_date) = 2020
    GROUP BY 1,2,3
)

SELECT DISTINCT customer_id, name
FROM cte
WHERE monthly_purchase >= 100
GROUP BY customer_id, name
HAVING COUNT(*) = 2