import json
import falcon


class JsonBodyParser(object):

    @staticmethod
    def process_request(req):
        if req.content_type == 'application/json':
            body = req.stream.read().decode('utf-8')
            try:
                req.context['data'] = json.loads(body)
            except ValueError:
                raise falcon.HTTPBadRequest('Bad Request', 'Request body is not valid \'application/json\'')
