-- This script lists all shows from the database by their rating
SELECT s.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows as s
INNER JOIN tv_show_ratings as r
ON s.id = r.show_id
GROUP BY s.id
ORDER BY rating DESC;
