from flask import Flask
from flask_restx import Api, Resource, fields


ns = None
api = None

def init(app: Flask) -> None:
    global api, ns
    api = Api(app, 
            version='2.1',
            title='Your app APIs',
            description='Retrive API document and testing.')
    ns = api.namespace('todos', description='TODO operations')
