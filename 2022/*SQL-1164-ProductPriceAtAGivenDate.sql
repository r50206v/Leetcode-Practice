WITH cte AS (
    SELECT 
        product_id, new_price, change_date,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS row_num
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT DISTINCT a.product_id, COALESCE(b.new_price, 10) AS price
FROM Products AS a
LEFT JOIN (SELECT * FROM cte WHERE row_num=1) AS b
ON a.product_id = b.product_id