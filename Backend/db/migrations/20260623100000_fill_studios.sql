-- migrate:up

INSERT INTO studios (id, name, country, founded_date, logo, description)
VALUES
(1, 'Warner Bros. Pictures', 'Estados Unidos', '1923-04-04', 'img/studios/warner_bros.png', 'Estudio de cine y televisión estadounidense.'),
(2, 'Paramount Pictures', 'Estados Unidos', '1912-05-08', 'img/studios/paramount.png', 'Uno de los estudios cinematográficos más antiguos de Hollywood.'),
(3, 'Sony Pictures Animation', 'Estados Unidos', '2002-05-09', 'img/studios/sony_animation.png', 'División de animación de Sony Pictures.'),
(4, 'Miramax Films', 'Estados Unidos', '1979-12-18', 'img/studios/miramax.png', 'Estudio cinematográfico independiente famoso por el cine de los 90.'),
(5, 'Pixar Animation Studios', 'Estados Unidos', '1986-02-03', 'img/studios/pixar.png', 'Estudio de animación por computadora subsidiario de Disney.');

-- migrate:down

DELETE FROM studios;