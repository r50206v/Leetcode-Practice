WITH cte AS (
    SELECT DISTINCT s.buyer_id 
    FROM Sales AS s
    LEFT JOIN Product AS p
    ON s.product_id = p.product_id
    WHERE p.product_name = 'iPhone'
)

SELECT DISTINCT s.buyer_id 
FROM Sales AS s
LEFT JOIN Product AS p
ON s.product_id = p.product_id
WHERE s.buyer_id NOT IN (SELECT buyer_id FROM cte)
    AND p.product_name = 'S8'