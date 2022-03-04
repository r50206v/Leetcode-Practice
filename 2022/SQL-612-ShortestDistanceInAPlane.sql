SELECT ROUND(distance, 2) AS shortest
FROM (
    SELECT 
        POW(POW(a.x - b.x, 2) + POW(a.y - b.y, 2), 0.5) AS distance
    FROM Point2D AS a, Point2D AS b
) AS t
WHERE distance > 0
ORDER BY distance ASC
LIMIT 1