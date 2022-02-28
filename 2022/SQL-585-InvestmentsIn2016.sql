SELECT ROUND(SUM(t1.tiv_2016), 2) AS tiv_2016
FROM Insurance AS t1
LEFT JOIN (
    SELECT tiv_2015, COUNT(*) AS most_common
    FROM Insurance
    GROUP BY tiv_2015
) AS t2
ON t1.tiv_2015 = t2.tiv_2015
LEFT JOIN (
    SELECT lat, lon, COUNT(*) AS count_loc
    FROM Insurance
    GROUP BY lat, lon
) AS t3
ON t1.lat = t3.lat
    AND t1.lon = t3.lon
WHERE t2.most_common >= 2
    AND t3.count_loc = 1