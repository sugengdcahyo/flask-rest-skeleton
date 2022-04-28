""" This module contains the 'index' Blueprint which organize and group,
views relateed to the index endpoint of HTTP REST API.
"""

from flask import Blueprint
from flask import make_response, jsonify
from flask_restx import fields
from flask_restx.resource import Resource
from src.swagger_api import api, ns
from src.database import es

bp = Blueprint('index', __name__, url_prefix='')

@bp.route('/test', methods=['GET'])
def index() -> dict:
    return {'message': 'oke'}


todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})
