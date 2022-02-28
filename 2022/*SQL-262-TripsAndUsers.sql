SELECT DISTINCT a.Request_at AS Day, 
    ROUND(SUM(a.Status) / COUNT(*), 2) AS `Cancellation Rate`
FROM (
    SELECT t.Request_at, CASE WHEN t.Status = "completed" THEN 0 ELSE 1 END AS `Status`
    FROM Trips AS t
    LEFT JOIN Users AS uc
    ON t.Client_Id = uc.Users_Id
    LEFT JOIN Users AS ud
    ON t.Driver_Id = ud.Users_Id
    WHERE uc.Banned = "No" 
        AND ud.Banned = "No"
        AND t.Request_at BETWEEN "2013-10-01" AND "2013-10-03"
) AS a
GROUP BY Request_at