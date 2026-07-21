-- migrate:up

INSERT INTO movie_people (id, movie_id, person_id, role)
VALUES
-- 1. Interstellar
(1, 1, 1, 'Director'),
(2, 1, 2, 'Actor'),
(3, 1, 3, 'Actor'),
(4, 1, 4, 'Actor'),

-- 2. The Dark Knight
(5, 2, 1, 'Director'),
(6, 2, 5, 'Actor'),
(7, 2, 6, 'Actor'),
(8, 2, 7, 'Actor'),

-- 3. Inception
(9, 3, 1, 'Director'),
(10, 3, 8, 'Actor'),
(11, 3, 9, 'Actor'),
(12, 3, 10, 'Actor'),

-- 4. Spider-Man: Into the Spider-Verse
(13, 4, 11, 'Director'),
(14, 4, 12, 'Actor'),
(15, 4, 13, 'Actor'),
(16, 4, 14, 'Actor'),

-- 5. Pulp Fiction
(17, 5, 15, 'Director'),
(18, 5, 16, 'Actor'),
(19, 5, 17, 'Actor'),
(20, 5, 18, 'Actor'),

-- 6. The Matrix
(21, 6, 19, 'Director'),
(22, 6, 20, 'Actor'),
(23, 6, 21, 'Actor'),
(24, 6, 22, 'Actor'),

-- 7. Whiplash
(25, 7, 23, 'Director'),
(26, 7, 24, 'Actor'),
(27, 7, 25, 'Actor'),

-- 8. Coco
(28, 8, 26, 'Director'),
(29, 8, 27, 'Actor'),
(30, 8, 28, 'Actor'),
(31, 8, 29, 'Actor');

-- migrate:down

DELETE FROM movie_people;