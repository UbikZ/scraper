import falcon
from app.middleware.body_parser import JSONBodyParser
from app.routes import Routes

api = falcon.API(middleware=[JSONBodyParser()])
Routes.build(api)
