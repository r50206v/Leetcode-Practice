SELECT u.user_id AS buyer_id, u.join_date, COALESCE(t.count_order, 0) AS orders_in_2019
FROM Users as u
LEFT JOIN (
    SELECT buyer_id, YEAR(order_date) AS order_year, COUNT(DISTINCT order_id) AS count_order
    FROM Orders
    WHERE YEAR(order_date) = 2019
    GROUP BY buyer_id, YEAR(order_date)
) AS t
ON u.user_id = t.buyer_id