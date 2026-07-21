#cineviews\models.py
from datetime import date
from typing import List, Optional

from sqlalchemy import (
    Integer, String, Text, Boolean, Float,
    ForeignKey, Date
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


# ==========================================
# SEX
# ==========================================

class Sex(Base):
    __tablename__ = "sexs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(30)
    )

    users: Mapped[List["User"]] = relationship(
        back_populates="sex"
    )

    people: Mapped[List["Person"]] = relationship(
        back_populates="sex"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


# ==========================================
# NATIONALITY
# ==========================================

class Nationality(Base):
    __tablename__ = "nationalities"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    demonym: Mapped[str] = mapped_column(
        String(100)
    )

    users: Mapped[List["User"]] = relationship(
        back_populates="nationality"
    )

    people: Mapped[List["Person"]] = relationship(
        back_populates="nationality"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "demonym": self.demonym
        }
# ==========================================
# USER
# ==========================================

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))

    reset_key: Mapped[Optional[str]] = mapped_column(String(100))
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    activation_key: Mapped[Optional[str]] = mapped_column(String(100))

    birth_date: Mapped[Optional[date]] = mapped_column(Date)
    profile_picture: Mapped[Optional[str]] = mapped_column(Text)
    bio: Mapped[Optional[str]] = mapped_column(Text)

    sex_id: Mapped[Optional[int]] = mapped_column(ForeignKey("sexs.id"))
    nationality_id: Mapped[Optional[int]] = mapped_column(ForeignKey("nationalities.id"))

    sex: Mapped[Optional["Sex"]] = relationship(back_populates="users")
    nationality: Mapped[Optional["Nationality"]] = relationship(back_populates="users")

    reviews: Mapped[List["Review"]] = relationship(back_populates="user")
    watched_movies: Mapped[List["WatchedMovie"]] = relationship(back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "status": self.status,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None,
            "profile_picture": self.profile_picture,
            "bio": self.bio,
            "sex": self.sex.to_dict() if self.sex else None,
            "nationality": self.nationality.to_dict() if self.nationality else None
        }


# ==========================================
# STUDIO
# ==========================================

class Studio(Base):
    __tablename__ = "studios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    country: Mapped[Optional[str]] = mapped_column(String(100))
    founded_date: Mapped[Optional[date]] = mapped_column(Date)
    logo: Mapped[Optional[str]] = mapped_column(Text)
    description: Mapped[Optional[str]] = mapped_column(Text)

    movies: Mapped[List["Movie"]] = relationship(back_populates="studio")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "founded_date": self.founded_date.isoformat() if self.founded_date else None,
            "logo": self.logo,
            "description": self.description
        }


# ==========================================
# PERSON
# ==========================================

class Person(Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    birth_date: Mapped[Optional[date]] = mapped_column(Date)
    biography: Mapped[Optional[str]] = mapped_column(Text)
    photo: Mapped[Optional[str]] = mapped_column(Text)

    sex_id: Mapped[Optional[int]] = mapped_column(ForeignKey("sexs.id"))
    nationality_id: Mapped[Optional[int]] = mapped_column(ForeignKey("nationalities.id"))

    sex: Mapped[Optional["Sex"]] = relationship(back_populates="people")
    nationality: Mapped[Optional["Nationality"]] = relationship(back_populates="people")

    movie_people: Mapped[List["MoviePeople"]] = relationship(back_populates="person")

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None,
            "biography": self.biography,
            "photo": self.photo,
            "sex": self.sex.to_dict() if self.sex else None,
            "nationality": self.nationality.to_dict() if self.nationality else None
        }

# ==========================================
# MOVIE
# ==========================================

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(255))
    release_date: Mapped[Optional[date]] = mapped_column(Date)
    synopsis: Mapped[str] = mapped_column(Text)
    genre: Mapped[str] = mapped_column(String(100))
    duration: Mapped[int] = mapped_column(Integer)
    average_rating: Mapped[float] = mapped_column(Float, default=0)

    poster: Mapped[str] = mapped_column(Text)
    trailer_url: Mapped[str] = mapped_column(Text)

    studio_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("studios.id")
    )

    studio: Mapped[Optional["Studio"]] = relationship(
        back_populates="movies"
    )

    reviews: Mapped[List["Review"]] = relationship(
        back_populates="movie"
    )

    watched_by: Mapped[List["WatchedMovie"]] = relationship(
        back_populates="movie"
    )

    movie_people: Mapped[List["MoviePeople"]] = relationship(
        back_populates="movie"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date.isoformat() if self.release_date else None,
            "synopsis": self.synopsis,
            "genre": self.genre,
            "duration": self.duration,
            "average_rating": self.average_rating,
            "poster": self.poster,
            "trailer_url": self.trailer_url,

            "studio": self.studio.to_dict() if self.studio else None,

            "people": [
                {
                    "role": mp.role,
                    "person": mp.person.to_dict() if mp.person else None
                }
                for mp in self.movie_people
            ],

            # Ahora cada review incluye también el usuario
            "reviews": [
                r.to_dict()
                for r in self.reviews
            ]
        }

# ==========================================
# MOVIE PEOPLE (RELACIÓN N:M)
# ==========================================

class MoviePeople(Base):
    __tablename__ = "movie_people"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    person_id: Mapped[int] = mapped_column(ForeignKey("people.id"))
    role: Mapped[str] = mapped_column(String(50))

    movie: Mapped["Movie"] = relationship(back_populates="movie_people")
    person: Mapped["Person"] = relationship(back_populates="movie_people")


# ==========================================
# REVIEW
# ==========================================

class Review(Base):

    __tablename__ = "reviews"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


    content: Mapped[str] = mapped_column(
        Text
    )


    rating: Mapped[float] = mapped_column(
        Float
    )


    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )


    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movies.id")
    )



    user: Mapped["User"] = relationship(
        back_populates="reviews"
    )



    movie: Mapped["Movie"] = relationship(
        back_populates="reviews"
    )




    def to_dict(self):

        return {


            "id": self.id,


            "content": self.content,


            "rating": self.rating,


            "user_id": self.user_id,


            "movie_id": self.movie_id,



            "user":

                self.user.to_dict()

                if self.user

                else None,



            "movie":

                {

                    "id": self.movie.id,

                    "title": self.movie.title,

                    "poster": self.movie.poster,

                    "genre": self.movie.genre,

                }

                if self.movie

                else None

        }
# ==========================================
# WATCHED MOVIES
# ==========================================

class WatchedMovie(Base):
    __tablename__ = "watched_movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    watched_date: Mapped[date] = mapped_column(Date)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))

    user: Mapped["User"] = relationship(back_populates="watched_movies")
    movie: Mapped["Movie"] = relationship(back_populates="watched_by")

    def to_dict(self):
        return {
            "id": self.id,
            "watched_date": self.watched_date.isoformat() if self.watched_date else None,
            "user_id": self.user_id,
            "movie_id": self.movie_id
        }