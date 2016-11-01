import falcon
from cerberus import Validator

fields = {
    'id': {
        'type': 'integer',
        'regex': '^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$',
        'required': True,
    },
    'idFeedItem': {
        'type': 'integer',
        'required': True,
    },
    'isEnabled': {
        'type': 'boolean',
        'required': True,
        'min': 0,
    }
}


class FeedItemValidate(object):
    @staticmethod
    def create(req, res, resource, params):
        test = Validator(fields)
        if not test.validate(req.context['data']):
            raise falcon.HTTPBadRequest('Bad request', test.errors)
