SELECT a.name, COALESCE(SUM(b.rest), 0) AS rest, COALESCE(SUM(b.paid), 0) AS paid,
    COALESCE(SUM(b.canceled), 0) AS canceled, COALESCE(SUM(b.refunded), 0) AS refunded
FROM Product AS a
LEFT JOIN Invoice AS b
ON a.product_id = b.product_id
GROUP BY 1
ORDER BY 1;