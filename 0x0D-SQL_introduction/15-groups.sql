-- this script lists the number of records with the same score in the table
SELECT score COUNT(score) as NUMBER GROUP BY score ORDER BY number DESC;