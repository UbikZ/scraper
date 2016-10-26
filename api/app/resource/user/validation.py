import falcon
from cerberus import Validator

fields = {
    'username': {
        'type': 'string',
        'required': True,
        'minlength': 3,
    },
    'type': {
        'type': 'list',
        'allowed': ['admin', 'user'],
        'required': True,
    },
    'email': {
        'type': 'string',
        'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        'required': True,
    },
}


class UserValidate(object):
    @staticmethod
    def create(req, res, resource, params):
        test = Validator(fields)
        if not test.validate(req.context['data']):
            raise falcon.HTTPBadRequest('Bad request', test.errors)
