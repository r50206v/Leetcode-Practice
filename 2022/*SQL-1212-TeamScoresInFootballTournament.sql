WITH cte AS (
    SELECT host_team AS team1, guest_team AS team2, host_goals AS team1_goals, guest_goals AS team2_goals
    FROM Matches
    UNION ALL
    SELECT guest_team AS team1, host_team AS team2, guest_goals AS team1_goals, host_goals AS team2_goals
    FROM Matches
)

SELECT Teams.team_id, Teams.team_name,
    COALESCE(SUM(t.points), 0) AS num_points
FROM Teams
LEFT JOIN (
    SELECT team1 AS team_id, 
    CASE WHEN team1_goals > team2_goals THEN 3
        WHEN team1_goals = team2_goals THEN 1
        ELSE 0 END AS points
    FROM cte
) AS t
ON t.team_id = Teams.team_id
GROUP BY 1, 2
ORDER BY num_points DESC, team_id ASC;