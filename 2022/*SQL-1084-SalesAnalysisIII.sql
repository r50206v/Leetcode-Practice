WITH cte AS (
    SELECT product_id, COUNT(DISTINCT QUARTER(sale_date)) AS count_sale
    FROM Sales
    GROUP BY product_id
)

SELECT DISTINCT s.product_id, p.product_name
FROM Sales AS s
LEFT JOIN Product AS p
ON s.product_id = p.product_id
LEFT JOIN cte 
ON s.product_id = cte.product_id
WHERE cte.count_sale = 1
    AND QUARTER(sale_date) = 1