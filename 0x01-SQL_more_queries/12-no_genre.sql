-- import DB dump from hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.shows_id is Null
ORDER BY tv_shows.title, tv_show_genres.genre_id;
