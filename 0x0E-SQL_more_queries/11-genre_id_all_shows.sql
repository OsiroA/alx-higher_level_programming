-- This script lists all shows contained in a specified database on the command lline
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows as t
LEFT JOIN tv_show_genre as g
ON t.id = g.show_id
ORDER BY t.title, g.genre_id ASC;
