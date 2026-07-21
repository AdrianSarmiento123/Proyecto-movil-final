#cineviews\apis\studio.py
import traceback
from flask import Blueprint, jsonify
from main.database import Session
from cineviews.models import Studio

api = Blueprint('cineviews_apis_studios', __name__)


# =====================================================
# LISTAR STUDIOS
# =====================================================
@api.route('/apis/v1/studios', methods=['GET'])
def fetch_all():

    session = Session()

    try:
        studios = session.query(Studio).all()

        return jsonify({
            "message": "Lista de estudios",
            "data": [s.to_dict() for s in studios],
            "success": True,
            "error": None
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": "Error al listar estudios",
            "data": None,
            "success": False,
            "error": str(e)
        }), 500

    finally:
        session.close()


# =====================================================
# DETALLE STUDIOS
# =====================================================
@api.route('/apis/v1/studios/<int:studio_id>', methods=['GET'])
def fetch_by_id(studio_id):

    session = Session()

    try:

        studio = session.query(Studio).filter(Studio.id == studio_id).first()

        if not studio:
            return jsonify({
                "message": "Studio no encontrado",
                "data": None,
                "success": False,
                "error": None
            }), 404

        return jsonify({
            "message": "Detalle studio",
            "data": studio.to_dict(),
            "success": True,
            "error": None
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": "Error al obtener studio",
            "data": None,
            "success": False,
            "error": str(e)
        }), 500

    finally:
        session.close()


# =====================================================
# PELÍCULAS DEL STUDIO
# =====================================================
@api.route('/apis/v1/studios/<int:studio_id>/movies', methods=['GET'])
def movies_by_studio(studio_id):

    session = Session()

    try:

        studio = session.query(Studio).filter(Studio.id == studio_id).first()

        if not studio:
            return jsonify({
                "message": "Studio no encontrado",
                "data": None,
                "success": False,
                "error": None
            }), 404

        return jsonify({
            "message": "Películas del studio",
            "data": [
                {
                    "id": m.id,
                    "title": m.title
                }
                for m in studio.movies
            ],
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