--  lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 
-- to-don arrangement
SELECT *
FROM second_table
WHERE `score` >= 90
ORDER BY `score` DESC;
