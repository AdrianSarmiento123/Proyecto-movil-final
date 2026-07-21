#cineviews\apis\people.py
import traceback
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import selectinload
from sqlalchemy import func

from main.database import Session
from cineviews.models import Person, MoviePeople

api = Blueprint('cineviews_apis_people', __name__)


# =====================================================
# LISTAR PERSONAS
# =====================================================
@api.route('/apis/v1/people', methods=['GET'])
def fetch_all():

    session = Session()

    try:
        people = session.query(Person).all()

        return jsonify({
            "message": "Lista de personas",
            "data": [p.to_dict() for p in people],
            "success": True,
            "error": None
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            "message": "Error al listar personas",
            "data": None,
            "success": False,
            "error": str(e)
        }), 500

    finally:
        session.close()


# =====================================================
# DETALLE PERSONA
# =====================================================
@api.route('/apis/v1/people/<int:person_id>', methods=['GET'])
def fetch_by_id(person_id):

    session = Session()

    try:

        person = (
            session.query(Person)
            .filter(Person.id == person_id)
            .first()
        )

        if not person:
            return jsonify({
                "message": "Persona no encontrada",
                "data": None,
                "success": False,
                "error": None
            }), 404

        return jsonify({
            "message": "Detalle de persona",
            "data": person.to_dict(),
            "success": True,
            "error": None
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            "message": "Error al obtener persona",
            "data": None,
            "success": False,
            "error": str(e)
        }), 500

    finally:
        session.close()


# =====================================================
# PELÍCULAS DE UNA PERSONA (OPTIMIZADO + FIX ROLE)
# =====================================================
@api.route('/apis/v1/people/<int:person_id>/movies', methods=['GET'])
def movies_by_person(person_id):

    session = Session()

    try:

        role = request.args.get("role")

        query = (
            session.query(MoviePeople)
            .options(selectinload(MoviePeople.movie))
            .filter(MoviePeople.person_id == person_id)
        )

        # FIX: case-insensitive
        if role:
            query = query.filter(
                func.lower(MoviePeople.role) == role.lower()
            )

        relations = query.all()

        data = []

        for r in relations:
            if r.movie:
                data.append({
                    "movie_id": r.movie.id,
                    "title": r.movie.title,
                    "role": r.role,
                    "poster": r.movie.poster
                })

        return jsonify({
            "message": "Películas de la persona",
            "data": data,
            "success": True,
            "error": None
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            "message": "Error al obtener películas",
            "data": None,
            "success": False,
            "error": str(e)
        }), 500

    finally:
        session.close()