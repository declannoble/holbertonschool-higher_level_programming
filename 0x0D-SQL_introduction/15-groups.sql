-- script to list number of records with same score

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
