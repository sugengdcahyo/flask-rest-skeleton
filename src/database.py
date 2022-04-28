from dotenv import load_dotenv

from elasticsearch import Elasticsearch
from elasticapm import Client

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import create_engine

import os

load_dotenv() # read .env attributes

es = None

def init(app: Flask) -> None:
    """ Initializing elasticsearch and others."""
    engine = create_engine(
        f"elasticsearch://?Server={os.environ.get('ELASTIC_SERVER')} \
                &Port={os.environ.get('ELASTIC_PORT')} \
                &User={os.environ.get('ELASTIC_USER')} \
                &Password={os.environ.get('ELASTIC_PASSWORD')}")

    global es
    db = SQLAlchemy(app)
    es = Elasticsearch(
            hosts = os.environ.get('ELASTIC_SERVER'),
            port = os.environ.get('ELASTIC_PORT'),
            http_auth = (
                os.environ.get('ELASTIC_USER'), 
                os.environ.get('ELASTIC_PASSWORD')
            ),
            send_get_body_as='POST',
            timeout=60
        )
    print("Elasticsearch connecting...")
    #apm = Client(
    #        app = app,
    #        server_url = os.environ.get('ELASTIC_APM_SERVER'),
    #        service_name = os.environ.get('ELASTIC_APM_SERVICE_NAME'),
    #        environment = os.environ.get('ELASTIC_APM_ENVIRONMENT'))
