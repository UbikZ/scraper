import falcon
from app.middleware.body_parser import JsonBodyParser

api = falcon.API(middleware=[JsonBodyParser()])
