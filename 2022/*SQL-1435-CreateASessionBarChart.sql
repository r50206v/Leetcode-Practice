WITH cte_bins (id, bin) AS (
    SELECT '1','[0-5>' FROM DUAL
    UNION
    SELECT '2','[5-10>' FROM DUAL
    UNION
    SELECT '3','[10-15>' FROM DUAL
    UNION
    SELECT '4','15 or more' FROM DUAL
)


SELECT a.bin, COUNT(b.session_id) AS total
FROM cte_bins AS a
LEFT JOIN (
    SELECT session_id, 
        CASE WHEN duration < 5*60 THEN "[0-5>"
            WHEN duration < 10*60 THEN "[5-10>"
            WHEN duration < 15*60 THEN "[10-15>"
            ELSE "15 or more" END AS bin
    FROM Sessions
) AS b
ON a.bin = b.bin
GROUP BY a.bin