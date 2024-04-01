-- lists the number of records with the same score in the table second_table
-- The result should display:
-- the score
-- the number of records for this score with the label number
SELECT `score`, COUNT(*) AS number
FROM `second_table`
GROUP BY `score`
HAVING count(*) > 1
ORDER BY `score` DESC;