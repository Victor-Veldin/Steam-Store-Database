USE steam_project;

-- 1. JOIN de 3 o más tablas
SELECT g.name, ge.genre_name, d.developer_name
FROM Game g
JOIN GameGenre gg ON g.appid = gg.appid
JOIN Genre ge ON gg.genre_id = ge.genre_id
JOIN GameDeveloper gd ON g.appid = gd.appid
JOIN Developer d ON gd.developer_id = d.developer_id
LIMIT 20;

-- 2. Agregación con GROUP BY
SELECT ge.genre_name, COUNT(*) AS total_games
FROM Genre ge
JOIN GameGenre gg ON ge.genre_id = gg.genre_id
GROUP BY ge.genre_name
ORDER BY total_games DESC;

-- 3. Subconsulta
SELECT name, price
FROM Game
WHERE price > (
    SELECT AVG(price)
    FROM Game
);

-- 4. Juegos con mejores ratings
SELECT name, positive_ratings, negative_ratings
FROM Game
ORDER BY positive_ratings DESC
LIMIT 10;

-- 5. Juegos gratis
SELECT g.name
FROM Game g
JOIN FreeGame f ON g.appid = f.appid
LIMIT 20;