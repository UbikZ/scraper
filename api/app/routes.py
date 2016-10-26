import sys
from app.resource.user.handler import *
from app.config import API_VERSION

routes = ['user']


class Routes(object):
    @staticmethod
    def build(api):
        for route in routes:
            api.add_route(
                '/v{0}/{1}'.format(API_VERSION, route),
                getattr(sys.modules['app.resource.{}.handler'.format(route)], '{}Resource'.format(route.title()))()
            )
