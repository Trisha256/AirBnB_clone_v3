#!/usr/bin/python3
"""api status"""
import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify
from api.v1.views import app_views
import sys
sys.path.append (models)


@app_views.route('/status', strict_slashes=False)
def returnstuff():
    """return stuff"""
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def stuff():
    """JSON Responses"""
    todos = {
        'states': State, 'users': User,
        'amenities': Amenity, 'cities': City,
        'places': Place, 'reviews': Review
        }

    for key in todos:
        todos[key] = storage.count(todos[key])
        return jsonify(todos)

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieve the number of each object by type"""
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
