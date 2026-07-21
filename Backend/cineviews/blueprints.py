#BackendCine\cineviews\blueprints.py
from .apis.movie import api as api_movies
from .apis.review import api as api_reviews
from .apis.user import api as api_users

# NUEVAS APIs (cuando las crees)
from .apis.people import api as api_people
from .apis.studio import api as api_studios

blueprints = [
    api_movies,
    api_reviews,
    api_users,
    api_people,
    api_studios,
]