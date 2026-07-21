-- migrate:up

INSERT INTO people (id, first_name, last_name, birth_date, biography, photo, sex_id, nationality_id)
VALUES

-- Interstellar & Nolan Movies
(1, 'Christopher', 'Nolan', '1970-07-30',
'Director, guionista y productor británico-estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/xuAIuYSmsUzKlUMBFGVZaWsY3DZ.jpg',
1, 2),

(2, 'Matthew', 'McConaughey', '1969-11-04',
'Actor y productor estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/lCySuYjhXix3FzQdS4oceDDrXKI.jpg',
1, 5),

(3, 'Anne', 'Hathaway', '1982-11-12',
'Actriz estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/nbccV2pMoyLTCeg5DQip24Eq0Jp.jpg',
2, 5),

(4, 'Jessica', 'Chastain', '1977-03-24',
'Actriz y productora estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/eQKnihReJeB9vQEa5gySzAlKfZt.jpg',
2, 5),


-- The Dark Knight
(5, 'Christian', 'Bale', '1974-01-30',
'Actor británico.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/7Pxez9J8fuPd2Mn9kex13YALrCQ.jpg',
1, 2),

(6, 'Heath', 'Ledger', '1979-04-04',
'Actor australiano.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/AdWKVqyWpkYSfKE5Gb2qn8JzHni.jpg',
1, 10),

(7, 'Gary', 'Oldman', '1958-03-21',
'Actor británico.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/yhaSM5habNNI1Tf4ALRwRk3VvSZ.jpg',
1, 2),


-- Inception
(8, 'Leonardo', 'DiCaprio', '1974-11-11',
'Actor y productor estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/mkdRcVIQl4WZhDf1vXKWTD7HZrZ.jpg',
1, 5),

(9, 'Joseph', 'Gordon-Levitt', '1981-02-17',
'Actor y director estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/z2FA8js799xqtfiFjBTicFYdfk.jpg',
1, 5),

(10, 'Elliot', 'Page', '1987-02-21',
'Actor canadiense.',
'https://upload.wikimedia.org/wikipedia/commons/5/57/Elliot_Page_2021.jpg',
1, 5),


-- Spider-Man: Into the Spider-Verse
(11, 'Bob', 'Persichetti', '1973-01-17',
'Director y animador estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/jmpNVUvvhJB2X2eOSKpveFnetM8.jpg',
1, 5),

(12, 'Shameik', 'Moore', '1995-05-04',
'Actor y cantante estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/8/8b/Shameik_Moore_2018.jpg',
1, 5),

(13, 'Hailee', 'Steinfeld', '1996-12-11',
'Actriz y cantante estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/6/67/Hailee_Steinfeld_2023.jpg',
2, 5),

(14, 'Mahershala', 'Ali', '1974-02-16',
'Actor estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/7/75/Mahershala_Ali_2016.jpg',
1, 5),


-- Pulp Fiction
(15, 'Quentin', 'Tarantino', '1963-03-27',
'Director, guionista y actor estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/1gjcpAa99FAOWGnrUvHEXXsRs7o.jpg',
1, 5),

(16, 'John', 'Travolta', '1954-02-18',
'Actor y cantante estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/1/1b/John_Travolta_Cannes_2018.jpg',
1, 5),

(17, 'Samuel L.', 'Jackson', '1948-12-21',
'Actor y productor estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/2/20/Samuel_L_Jackson_2019.jpg',
1, 5),

(18, 'Uma', 'Thurman', '1970-04-29',
'Actriz y modelo estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/8/8e/Uma_Thurman_Cannes_2017.jpg',
2, 5),


-- The Matrix
(19, 'Lana', 'Wachowski', '1965-06-21',
'Directora y guionista estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/rCScAjSpeKA19BLNR07MqNNeeTT.jpg',
2, 5),

(20, 'Keanu', 'Reeves', '1964-09-02',
'Actor canadiense.',
'https://upload.wikimedia.org/wikipedia/commons/d/d0/Keanu_Reeves_2022.jpg',
1, 5),

(21, 'Laurence', 'Fishburne', '1961-07-30',
'Actor y productor estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/a/a5/Laurence_Fishburne_2019.jpg',
1, 5),

(22, 'Carrie-Anne', 'Moss', '1967-08-21',
'Actriz canadiense.',
'https://upload.wikimedia.org/wikipedia/commons/3/31/Carrie-Anne_Moss_2016.jpg',
2, 5),


-- Whiplash
(23, 'Damien', 'Chazelle', '1985-01-19',
'Director y guionista estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/14kRZ3XxNMyBv717YQSXr3wCucy.jpg',
1, 5),

(24, 'Miles', 'Teller', '1987-02-20',
'Actor estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/9/95/Miles_Teller_2016.jpg',
1, 5),

(25, 'J.K.', 'Simmons', '1955-01-09',
'Actor estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/4/45/J._K._Simmons_2017.jpg',
1, 5),


-- Coco
(26, 'Lee', 'Unkrich', '1967-08-08',
'Director y montajista estadounidense.',
'https://media.themoviedb.org/t/p/w300_and_h450_face/crb297utC6W4HSstOe5djDPTwEN.jpg',
1, 5),

(27, 'Anthony', 'Gonzalez', '2004-09-23',
'Actor y cantante estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/0/0d/Anthony_Gonzalez_2017.jpg',
1, 5),

(28, 'Gael', 'García Bernal', '1978-11-30',
'Actor y director mexicano.',
'https://upload.wikimedia.org/wikipedia/commons/8/8c/Gael_Garcia_Bernal_2018.jpg',
1, 5),

(29, 'Benjamin', 'Bratt', '1963-12-16',
'Actor estadounidense.',
'https://upload.wikimedia.org/wikipedia/commons/9/9a/Benjamin_Bratt_2019.jpg',
1, 5);


-- migrate:down

DELETE FROM people;