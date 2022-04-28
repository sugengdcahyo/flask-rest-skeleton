from flask_restx import (
        Namespace, Resource, fields
    )

api = Namespace(
        'tests', description='API index testing'
    )

cat = api.model('Tests', {
            'id': fields.String(required=True, description='The test identifier'),
            'name': fields.String(required=True, description='The test name')
        }
    )
CATS = [
        {'id': 'felix', 'name': 'Felix'}
    ]

@api.route('/')
class TestList(Resource):
    
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all tests'''
        return CATS


@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'The cat identifier')
class Test(Resource):

    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, **kwargs):
        ''' Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == kwargs['id']:
                return cat
            api.abort(404)

