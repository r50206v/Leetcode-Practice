SELECT p.product_name, o.total_units AS unit
FROM (
    SELECT product_id, SUM(unit) AS total_units
    FROM Orders
    WHERE YEAR(order_date) = 2020
        AND MONTH(order_date) = 2
    GROUP BY product_id
    HAVING total_units >= 100
) AS o
LEFT JOIN Products AS p
ON o.product_id = p.product_id