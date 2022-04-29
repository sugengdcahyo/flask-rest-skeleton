from flask_restx import (
        Namespace, Resource, fields
    )

from ..swagger import cats

CATS = [
        {'id': 'felix', 'name': 'Felix'}
    ]

@cats.api.route('/')
class TestList(Resource):
    
    @cats.api.doc('list_cats')
    @cats.api.marshal_list_with(cats.model)
    def get(self):
        '''List all tests'''
        return CATS


@cats.api.route('/<id>')
@cats.api.param('id', 'The cat identifier')
@cats.api.response(404, 'The cat identifier')
class Test(Resource):

    @cats.api.doc('get_cat')
    @cats.api.marshal_with(cats.model)
    def get(self, **kwargs):
        ''' Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == kwargs['id']:
                return cat
            cats.api.abort(404)

