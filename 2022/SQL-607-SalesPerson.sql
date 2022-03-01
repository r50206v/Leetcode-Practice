SELECT name 
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT sales_id
    FROM Orders AS o
    LEFT JOIN Company AS c
    ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)