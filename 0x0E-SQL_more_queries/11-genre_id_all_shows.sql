-- This script lists all shows contained in a specified database on the command lline
SELECT t.title, g.genre_id
FROM tv_shows AS t
	LEFT JOIN tv_show_genre AS g
	ON t.id = g.show_id
ORDER BY t.title, g.genre_id ASC;
