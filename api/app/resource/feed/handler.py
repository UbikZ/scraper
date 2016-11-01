import falcon
import json
from app.resource.feed.validation import FeedValidate
from app.helper.hook import Hook


@falcon.before(Hook.open_cursor)
@falcon.after(Hook.close_cursor)
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
