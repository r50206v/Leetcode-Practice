SELECT DISTINCT Num AS ConsecutiveNum
FROM 
    Logs AS l1, Logs AS l2, Logs AS l3
WHERE 
    l1.Id + 1 = l2.Id
    AND l2.Id + 1 = l3.Id
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num;


SELECT DISTINCT a.Num AS ConsecutiveNums
FROM (
    SELECT Num, 
        LAG(Num) OVER (ORDER BY Id) AS `lag`, 
        LEAD(Num) OVER (ORDER BY Id) AS `lead`
    FROM Logs
) AS a
WHERE a.Num = a.lag 
    AND a.Num = a.lead;