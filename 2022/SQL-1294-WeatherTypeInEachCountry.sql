WITH cte AS (
    SELECT country_id, AVG(weather_state) AS avg_weather
    FROM Weather 
    WHERE YEAR(day) = 2019 
        AND MONTH(day) = 11
    GROUP BY country_id
)

SELECT c.country_name, 
    CASE WHEN cte.avg_weather <= 15 THEN 'Cold' 
        WHEN cte.avg_weather >= 25 THEN 'Hot'
        ELSE "Warm" END AS weather_type
FROM cte 
LEFT JOIN Countries AS c
ON cte.country_id = c.country_id