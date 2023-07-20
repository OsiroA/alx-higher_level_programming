-- THIS SCRIPT DISPLAYS THE TOP 3 CITIES AND TEMPERATIURES IN JULY AND AUGUST
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;