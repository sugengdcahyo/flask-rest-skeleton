from flask_restx import Namespace, fields

api = Namespace(
        'Cats', description='Endpoint of cats.')

model = api.model('Cats', {
        'id': fields.String(required=True, description='The cat identifier'),
        'name': fields.String(required=True, description='The cat name')
    })
