import sys
import psycopg2
from urlparse import urlparse
from app.config import DB_CONN_STRING
from app.resource.feed.model import *


class Database(object):
    @staticmethod
    def connection():
        parsed = urlparse(DB_CONN_STRING)
        user = parsed.username
        password = parsed.password
        host = parsed.hostname
        port = parsed.port
        database = parsed.path.strip('/')

        connection = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
        connection.set_session(autocommit=True)

        return connection

    @staticmethod
    def create_model():
        for model in ['feed']:
            getattr(sys.modules['app.resource.{}.model'.format(model)], '{}Model'.format(model.title()))()
