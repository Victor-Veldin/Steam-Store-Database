USE steam_project;

-- 1. JOIN de 3 o más tablas
-- Muestra juegos junto con su género y desarrollador.
SELECT 
    g.name AS game_name,
    ge.genre_name,
    d.developer_name
FROM Game g
JOIN GameGenre gg ON g.appid = gg.appid
JOIN Genre ge ON gg.genre_id = ge.genre_id
JOIN GameDeveloper gd ON g.appid = gd.appid
JOIN Developer d ON gd.developer_id = d.developer_id
LIMIT 20;


-- 2. Consulta con agregación GROUP BY
-- Cuenta cuántos juegos hay por género.
SELECT 
    ge.genre_name,
    COUNT(*) AS total_games
FROM Genre ge
JOIN GameGenre gg ON ge.genre_id = gg.genre_id
GROUP BY ge.genre_name
ORDER BY total_games DESC;


-- 3. Subconsulta
-- Muestra juegos cuyo precio es mayor que el precio promedio.
SELECT 
    name,
    price
FROM Game
WHERE price > (
    SELECT AVG(price)
    FROM Game
)
ORDER BY price DESC
LIMIT 20;


-- 4. Top Rated Games
-- Muestra los juegos con más ratings positivos.
SELECT 
    name,
    positive_ratings,
    negative_ratings
FROM Game
ORDER BY positive_ratings DESC
LIMIT 10;


-- 5. Juegos disponibles por plataforma
-- Muestra juegos disponibles en Windows.
SELECT 
    g.name AS game_name,
    p.platform_name
FROM Game g
JOIN GamePlatform gp ON g.appid = gp.appid
JOIN Platform p ON gp.platform_id = p.platform_id
WHERE p.platform_name = 'windows'
LIMIT 20;


-- 6. Most Played Games
-- Muestra los juegos con mayor tiempo promedio de juego.
SELECT 
    name,
    average_playtime
FROM Game
ORDER BY average_playtime DESC
LIMIT 20;


-- 7. Most Expensive Games
-- Muestra los juegos más caros.
SELECT 
    name,
    price
FROM Game
ORDER BY price DESC
LIMIT 20;


-- 8. Most Achievements
-- Muestra los juegos con más achievements.
SELECT 
    name,
    achievements
FROM Game
ORDER BY achievements DESC
LIMIT 20;


-- 9. Dashboard: total de juegos
SELECT COUNT(*) AS total_games
FROM Game;


-- 10. Dashboard: total de géneros
SELECT COUNT(*) AS total_genres
FROM Genre;


-- 11. Dashboard: total de desarrolladores
SELECT COUNT(*) AS total_developers
FROM Developer;


-- 12. Dashboard: total de publicadores
SELECT COUNT(*) AS total_publishers
FROM Publisher;


-- 13. Dashboard: total de plataformas
SELECT COUNT(*) AS total_platforms
FROM Platform;