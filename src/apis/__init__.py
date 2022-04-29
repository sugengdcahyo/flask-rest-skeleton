from flask_restx import Api

from .index import cats

api = Api(
        title='My Test Documents',
        version='0.1',
        description='A description',
    )

api.add_namespace(cats.api, path='/cats')
