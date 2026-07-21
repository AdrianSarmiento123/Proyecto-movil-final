# cineviews/apis/movie.py

import traceback

from flask import Blueprint, jsonify, request
from sqlalchemy.orm import selectinload

from main.database import Session
from main.middlewares import jwt_required

from cineviews.models import Movie, Review, MoviePeople

api = Blueprint('cineviews_apis_movies', __name__)


# =====================================================
# LISTAR TODAS LAS PELÍCULAS
# =====================================================
@api.route('/apis/v1/movies', methods=['GET'])
# @jwt_required
def fetch_all():

    session = Session()

    try:

        movies = (
            session.query(Movie)
            .options(
                selectinload(Movie.studio),
                selectinload(Movie.movie_people),
                selectinload(Movie.reviews)
            )
            .all()
        )

        return jsonify({
            'message': 'Lista de películas',
            'data': [movie.to_dict() for movie in movies],
            'success': True,
            'error': None
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            'message': 'Ocurrió un error al listar películas',
            'data': None,
            'success': False,
            'error': str(e)
        }), 500

    finally:
        session.close()


# =====================================================
# BUSCAR POR GÉNERO
# =====================================================
@api.route('/apis/v2/movies', methods=['GET'])
# @jwt_required
def search_by_genre():

    session = Session()

    try:

        genre = request.args.get('genre')

        query = (
            session.query(Movie)
            .options(
                selectinload(Movie.studio),
                selectinload(Movie.movie_people),
                selectinload(Movie.reviews)
            )
        )

        if genre:
            query = query.filter(Movie.genre.ilike(f'%{genre}%'))

        movies = query.all()

        return jsonify({
            'message': 'Películas filtradas correctamente',
            'data': [m.to_dict() for m in movies],
            'success': True,
            'error': None
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            'message': 'Ocurrió un error al filtrar películas',
            'data': None,
            'success': False,
            'error': str(e)
        }), 500

    finally:
        session.close()


# =====================================================
# BUSCAR POR TÍTULO
# =====================================================
@api.route('/apis/v3/movies', methods=['GET'])
# @jwt_required
def search_by_title():

    session = Session()

    try:

        title = request.args.get('title')

        query = (
            session.query(Movie)
            .options(
                selectinload(Movie.studio),
                selectinload(Movie.movie_people),
                selectinload(Movie.reviews)
            )
        )

        if title:
            query = query.filter(Movie.title.ilike(f'%{title}%'))

        movies = query.all()

        return jsonify({
            'message': 'Películas encontradas correctamente',
            'data': [m.to_dict() for m in movies],
            'success': True,
            'error': None
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            'message': 'Ocurrió un error al buscar películas',
            'data': None,
            'success': False,
            'error': str(e)
        }), 500

    finally:
        session.close()


# =====================================================
# LISTAR PELÍCULAS CON REVIEWS (OPTIMIZADO)
# =====================================================
@api.route('/apis/v4/movies', methods=['GET'])
# @jwt_required
def fetch_all_join():

    session = Session()

    try:

        movies = (
            session.query(Movie)
            .options(
                selectinload(Movie.studio),
                selectinload(Movie.movie_people),
                selectinload(Movie.reviews)
            )
            .all()
        )

        return jsonify({
            'message': 'Lista de películas con relaciones',
            'data': [m.to_dict() for m in movies],
            'success': True,
            'error': None
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            'message': 'Ocurrió un error al listar películas',
            'data': None,
            'success': False,
            'error': str(e)
        }), 500

    finally:
        session.close()


# =====================================================
# DETALLE DE UNA PELÍCULA
# =====================================================
@api.route('/apis/v1/movies/<int:movie_id>', methods=['GET'])
# @jwt_required
def fetch_by_id(movie_id):

    session = Session()

    try:

        movie = (
            session.query(Movie)
            .options(
                selectinload(Movie.studio),
                selectinload(Movie.movie_people),
                selectinload(Movie.reviews)
            )
            .filter(Movie.id == movie_id)
            .first()
        )

        if movie is None:
            return jsonify({
                'message': 'Película no encontrada',
                'data': None,
                'success': False,
                'error': None
            }), 404

        return jsonify({
            'message': 'Detalle de película',
            'data': movie.to_dict(),
            'success': True,
            'error': None
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            'message': 'Ocurrió un error al obtener la película',
            'data': None,
            'success': False,
            'error': str(e)
        }), 500

    finally:
        session.close()

