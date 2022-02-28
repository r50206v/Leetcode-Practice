SELECT c2.name AS country
FROM Person p
JOIN Calls c1
ON p.id=c1.caller_id OR p.id=c1.callee_id
JOIN Country c2
ON c2.country_code=SUBSTRING(p.phone_number,1,3)
GROUP BY 1
HAVING SUM(duration)/COUNT(duration)>( SELECT SUM(duration)/COUNT(duration) FROM Calls )