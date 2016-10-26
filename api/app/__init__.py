import falcon
from app.middleware.body_parser import JsonBodyParser
from app.routes import Routes

api = falcon.API(middleware=[JsonBodyParser()])
Routes.build(api)
