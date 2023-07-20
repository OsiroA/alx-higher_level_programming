-- This script lists all shows from the database by their rating
SELECT s.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows AS s
INNER JOIN tv_show_ratings AS r
ON tv_shows.id = r.show_id
GROUP BY r.id
ORDER BY rating DESC;
