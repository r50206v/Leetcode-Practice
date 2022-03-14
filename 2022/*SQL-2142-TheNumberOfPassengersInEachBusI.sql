SELECT bus_id, COUNT(passenger_id) AS passengers_cnt
FROM (
    SELECT bus_id, arrival_time, 
        COALESCE(LAG(arrival_time) OVER (ORDER BY arrival_time ASC), 0) AS last_arrival
    FROM Buses
) AS b
LEFT JOIN Passengers AS p
ON b.last_arrival < p.arrival_time
    AND p.arrival_time <= b.arrival_time
GROUP BY 1
ORDER BY 1;