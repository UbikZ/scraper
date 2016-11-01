import falcon
from app.middleware.body_parser import JSONBodyParser
from app.middleware.db_handler import DatabaseHandler
from app.helper.database import Database
from app.routes import Routes

Database.create_model()
db = Database.connection()
api = falcon.API(middleware=[JSONBodyParser(), DatabaseHandler(db)])
Routes.build(api)
