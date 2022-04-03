SELECT product_name, sale_date, COUNT(sale_id) AS total
FROM (
    SELECT LOWER(TRIM(product_name)) AS product_name, 
        DATE_FORMAT(sale_date, '%Y-%m') AS sale_date,
        sale_id
    FROM Sales
) AS t
GROUP BY product_name, sale_date
ORDER BY product_name ASC, sale_date ASC