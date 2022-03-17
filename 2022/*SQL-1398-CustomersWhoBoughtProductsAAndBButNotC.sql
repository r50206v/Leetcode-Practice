SELECT customer_id, customer_name
FROM Customers
WHERE customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'A')
    AND customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'B')
    AND customer_id NOT IN (SELECT customer_id FROM Orders WHERE product_name = 'C')



with temp as (
    select c.customer_id, c.customer_name, product_name 
    from Customers c 
    left join Orders o 
    on c.customer_id = o.customer_id
)

select distinct customer_id, customer_name from temp where product_name in ('A')
INTERSECT
select distinct customer_id, customer_name from temp where product_name in ('B')
EXCEPT
select distinct customer_id, customer_name from temp where product_name in ('C')