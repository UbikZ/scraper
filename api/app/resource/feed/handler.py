import falcon
import json
from app.resource.feed.validation import FeedValidate


class FeedResource(object):
    @falcon.before(FeedValidate.creation)
    def on_post(self, req, res):
        res.status = falcon.HTTP_201
        res.body = json.dumps(req.context['data'])

    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = json.dumps({
            'test': 'get2'
        })
