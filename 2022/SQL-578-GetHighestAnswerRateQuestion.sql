SELECT t.question_id AS survey_log
FROM (
    SELECT question_id, q_num, SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) AS answer_count
    FROM SurveyLog
    GROUP BY question_id, q_num
    ORDER BY answer_count DESC
    LIMIT 1
) AS t