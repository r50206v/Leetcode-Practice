SELECT team_name, COUNT(*) AS matches_played, 
    SUM(CASE WHEN home_team_id = team_id THEN home_team_points ELSE 0 END
        + CASE WHEN away_team_id = team_id THEN away_team_points ELSE 0 END) AS points,
    SUM(CASE WHEN home_team_id = team_id THEN home_team_goals ELSE 0 END 
        + CASE WHEN away_team_id = team_id THEN away_team_goals ELSE 0 END) AS goal_for,
    SUM(CASE WHEN home_team_id != team_id THEN home_team_goals ELSE 0 END 
        + CASE WHEN away_team_id != team_id THEN away_team_goals ELSE 0 END) AS goal_against,
    SUM(CASE WHEN home_team_id = team_id THEN home_team_goals ELSE 0 END 
        + CASE WHEN away_team_id = team_id THEN away_team_goals ELSE 0 END) 
    - SUM(CASE WHEN home_team_id != team_id THEN home_team_goals ELSE 0 END 
        + CASE WHEN away_team_id != team_id THEN away_team_goals ELSE 0 END) AS goal_diff
FROM (
    SELECT t.*, m.*,
        CASE WHEN home_team_goals > away_team_goals THEN 3 
            WHEN home_team_goals = away_team_goals THEN 1 
            ELSE 0 END AS home_team_points,
        CASE WHEN away_team_goals > home_team_goals THEN 3 
            WHEN home_team_goals = away_team_goals THEN 1 
            ELSE 0 END AS away_team_points
    FROM Matches AS m
    LEFT JOIN Teams AS t
    ON m.home_team_id = t.team_id
        OR m.away_team_id = t.team_id
) AS final
GROUP BY team_name
ORDER BY points DESC, goal_diff DESC, team_name ASC