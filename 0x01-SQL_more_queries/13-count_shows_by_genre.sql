-- import DB dump from hbtn_0d_tvshows
-- list genres and display number of shows linked
SELECT tv_show_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres LEFT JOIN tv_genres
ON tv_genres.id = genre_id
GROUP BY genre_id ORDER BY number_of_shows DESC;
