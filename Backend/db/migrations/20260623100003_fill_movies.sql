-- migrate:up

INSERT INTO movies (
    id,
    title,
    release_date,
    synopsis,
    genre,
    duration,
    average_rating,
    poster,
    trailer_url,
    studio_id
)
VALUES
(
    1,
    'Interstellar',
    '2014-11-07',
    'Un grupo de exploradores viaja a traves de un agujero de gusano en el espacio para intentar asegurar la supervivencia de la humanidad.',
    'Ciencia Ficcion',
    169,
    4.8,
    'https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
    'https://www.youtube.com/watch?v=zSWdZVtXT7E',
    2
),
(
    2,
    'The Dark Knight',
    '2008-07-18',
    'Batman se enfrenta a su enemigo mas complejo y caotico: el Joker, quien busca sumergir a Ciudad Gotica en el caos.',
    'Accion',
    152,
    4.9,
    'https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg',
    'https://www.youtube.com/watch?v=EXeTwQWrcwY',
    1
),
(
    3,
    'Inception',
    '2010-07-16',
    'Un ladron que roba secretos corporativos a traves del uso de la tecnologia de intercambio de suenos recibe la tarea inversa de implantar una idea.',
    'Ciencia Ficcion',
    148,
    4.7,
    'https://image.tmdb.org/t/p/w600_and_h900_face/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg',
    'https://www.youtube.com/watch?v=YoHD9XEInc0',
    1
),
(
    4,
    'Spider-Man: Into the Spider-Verse',
    '2018-12-14',
    'El joven Miles Morales se convierte en el nuevo Spider-Man y une fuerzas con heroes aracnidos de otras dimensiones para salvar el multiverso.',
    'Animacion',
    117,
    4.8,
    'https://image.tmdb.org/t/p/w600_and_h900_face/iiZZdoQBEYBv6id8su7ImL0oCbD.jpg',
    'https://www.youtube.com/watch?v=g4Hbz2jLxvQ',
    3
),
(
    5,
    'Pulp Fiction',
    '1994-10-14',
    'Las vidas de dos matones a sueldo, la esposa de un ganster, un boxeador y una pareja de atrancadores de restaurantes se entrelazan en cuatro historias.',
    'Crimen',
    154,
    4.6,
    'https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg',
    'https://www.youtube.com/watch?v=s7EdQ4FqbhY',
    4
),
(
    6,
    'The Matrix',
    '1999-03-31',
    'Un programador e informatico descubre que el mundo en el que vive es una simulacion virtual controlada por inteligencia artificial.',
    'Ciencia Ficcion',
    136,
    4.7,
    'https://image.tmdb.org/t/p/w600_and_h900_face/dXNAPwY7VrqMAo51EKhhCJfaGb5.jpg',
    'https://www.youtube.com/watch?v=vKQi3bBA1y8',
    1
),
(
    7,
    'Whiplash',
    '2014-10-10',
    'Un joven y ambicioso baterista de jazz se inscribe en un elitista conservatorio donde su despiadado instructor no se detendra ante nada para lograr su potencial.',
    'Drama',
    107,
    4.5,
    'https://image.tmdb.org/t/p/w600_and_h900_face/7fn624j5lj3xTme2SgiLCeuedmO.jpg',
    'https://www.youtube.com/watch?v=7d_jQyC8D_E',
    2
),
(
    8,
    'Coco',
    '2017-10-27',
    'Miguel, un aspirante a musico, se enfrenta a la prohibicion ancestral de su familia contra la musica y entra a la impresionante Tierra de los Muertos.',
    'Animacion',
    105,
    4.8,
    'https://image.tmdb.org/t/p/w600_and_h900_face/6Ryitt95xrO8KXuqRGm1fUuNwqF.jpg',
    'https://www.youtube.com/watch?v=Rvr68u6k5sI',
    5
);

-- migrate:down

DELETE FROM movies;