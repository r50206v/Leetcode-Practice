SELECT ad_id, 
    COALESCE(ROUND(SUM(click) / SUM(click + `view`) * 100, 2), 0) AS ctr
FROM (
    SELECT ad_id, 
        CASE WHEN action = "Clicked" THEN 1 ELSE 0 END AS click, 
        CASE WHEN action = "Viewed" THEN 1 ELSE 0 END AS `view`
    FROM Ads
) AS t
GROUP BY 1
ORDER BY ctr DESC, ad_id ASC