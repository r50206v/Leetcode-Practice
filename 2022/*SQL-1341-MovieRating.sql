WITH movie_rating AS (
    SELECT a.movie_id, b.title, AVG(a.rating) AS avg_rating
    FROM MovieRating AS a
    LEFT JOIN Movies AS b
    ON a.movie_id = b.movie_id
    WHERE YEAR(a.created_at) = 2020
        AND MONTH(a.created_at) = 2
    GROUP BY a.movie_id, b.title
), 
    user_rating AS (
    SELECT a.user_id, b.name, COUNT(a.created_at) AS rating_count
    FROM MovieRating AS a
    LEFT JOIN Users AS b
    ON a.user_id = b.user_id
    GROUP BY a.user_id, b.name
)


SELECT * FROM (
    SELECT name AS results
    FROM user_rating
    ORDER BY rating_count DESC, name ASC
    LIMIT 1
) AS a
UNION ALL
SELECT * FROM (
    SELECT title AS results
    FROM movie_rating
    ORDER BY avg_rating DESC, title ASC
    LIMIT 1
) AS b