-- This script lists all the cities of california that can e found in the database
SELECT id, name
FROM cities, states
WHERE state_id IN (
	SELECT id
	FROM states
	WHERE name = 'California')
ORDER BY cities.id ASC;
