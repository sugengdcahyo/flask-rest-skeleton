from flask_restx import Api

from .index import api as cats

api = Api(
        title='My Test Documents',
        version='0.1',
        description='A description'
    )

api.add_namespace(cats, path='/cats')
