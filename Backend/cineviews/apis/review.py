# cineviews/apis/review.py

import traceback

from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload

from main.database import Session
from cineviews.models import Review, Movie

api = Blueprint('cineviews_apis_reviews', __name__)


# =====================================================
# LISTAR REVIEWS
# =====================================================
@api.route('/apis/v1/reviews', methods=['GET'])
def fetch_all():

    session = Session()

    try:

        reviews = (
            session.query(Review)
            .options(
                joinedload(Review.user),
                joinedload(Review.movie)
            )
            .all()
        )

        return jsonify({
            "message": "Lista de reviews",
            "data": [r.to_dict() for r in reviews],
            "success": True,
            "error": None
        })

    except Exception as e:

        traceback.print_exc()

        return jsonify({
            "message": "Error al listar reviews",
            "data": None,
            "success": False,
            "error": str(e)
        }), 500

    finally:

        session.close()


# =====================================================
# REVIEWS POR PELÍCULA
# =====================================================
@api.route('/apis/v1/reviews/movie/<int:movie_id>', methods=['GET'])
def fetch_by_movie(movie_id):

    session = Session()

    try:

        reviews = (
            session.query(Review)
            .options(
                joinedload(Review.user)
            )
            .filter(
                Review.movie_id == movie_id
            )
            .all()
        )

        return jsonify({
            "message": "Reviews de la película",
            "data": [r.to_dict() for r in reviews],
            "success": True,
            "error": None
        })

    except Exception as e:

        traceback.print_exc()

        return jsonify({
            "message": "Error al filtrar reviews",
            "data": None,
            "success": False,
            "error": str(e)
        }), 500

    finally:

        session.close()


# =====================================================
# CREAR REVIEW
# =====================================================
@api.route('/apis/v1/reviews', methods=['POST'])
def create_review():

    session = Session()

    try:

        data = request.get_json() or {}

        # ==========================================
        # VALIDACIONES
        # ==========================================

        if not data.get("content") or not data.get("rating"):

            return jsonify({
                "message": "content y rating son obligatorios",
                "data": None,
                "success": False,
                "error": "Validation error"
            }), 400

        if not data.get("user_id") or not data.get("movie_id"):

            return jsonify({
                "message": "user_id y movie_id son obligatorios",
                "data": None,
                "success": False,
                "error": "Validation error"
            }), 400

        rating = float(data["rating"])

        if rating < 1 or rating > 5:

            return jsonify({
                "message": "La calificación debe estar entre 1 y 5",
                "data": None,
                "success": False,
                "error": "Validation error"
            }), 400

        # ==========================================
        # SOLO UNA REVIEW POR USUARIO Y PELÍCULA
        # ==========================================

        existing_review = (
            session.query(Review)
            .filter(
                Review.user_id == int(data["user_id"]),
                Review.movie_id == int(data["movie_id"])
            )
            .first()
        )

        if existing_review:

            return jsonify({
                "message": "Ya calificaste esta película",
                "data": None,
                "success": False,
                "error": "Duplicate review"
            }), 409

        # ==========================================
        # CREAR REVIEW
        # ==========================================

        review = Review(
            content=data["content"].strip(),
            rating=rating,
            user_id=int(data["user_id"]),
            movie_id=int(data["movie_id"])
        )

        session.add(review)
        session.commit()

        # ==========================================
        # RECARGAR REVIEW CON USUARIO
        # ==========================================

        review = (
            session.query(Review)
            .options(
                joinedload(Review.user)
            )
            .filter(
                Review.id == review.id
            )
            .first()
        )

        # ==========================================
        # RECALCULAR PROMEDIO DE LA PELÍCULA
        # ==========================================

        movie = (
            session.query(Movie)
            .options(
                joinedload(Movie.reviews)
            )
            .filter(
                Movie.id == review.movie_id
            )
            .first()
        )

        if movie:

            ratings = [
                r.rating
                for r in movie.reviews
            ]

            movie.average_rating = (
                sum(ratings) / len(ratings)
                if ratings
                else 0
            )

            session.commit()
            session.refresh(movie)

        return jsonify({
            "message": "Review creada correctamente",
            "data": review.to_dict(),
            "success": True,
            "error": None
        }), 201

    except Exception as e:

        session.rollback()

        traceback.print_exc()

        return jsonify({
            "message": "Error al crear review",
            "data": None,
            "success": False,
            "error": str(e)
        }), 500

    finally:

        session.close()
# =====================================================
# REVIEWS POR USUARIO
# =====================================================
@api.route('/apis/v1/reviews/user/<int:user_id>', methods=['GET'])
def fetch_by_user(user_id):

    session = Session()

    try:

        reviews = (
            session.query(Review)
            .options(
                joinedload(Review.movie),
                joinedload(Review.user)
            )
            .filter(
                Review.user_id == user_id
            )
            .all()
        )


        return jsonify({

            "message": "Reviews del usuario",

            "data": [
                r.to_dict()
                for r in reviews
            ],

            "success": True,

            "error": None

        })


    except Exception as e:


        traceback.print_exc()


        return jsonify({

            "message": "Error al buscar reviews del usuario",

            "data": None,

            "success": False,

            "error": str(e)

        }),500


    finally:

        session.close()