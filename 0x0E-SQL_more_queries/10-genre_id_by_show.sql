-- creates a table in a database
-- if it doesn't exist create it
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres
INNER JOIN tv_shows ON tv_shows.id=tv_show_genres.genre_id ORDER BY
tv_shows.title, tv_show_genres.genre_id;
