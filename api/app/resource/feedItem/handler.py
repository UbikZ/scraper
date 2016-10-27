import falcon
import json


class FeedItemResource(object):
    # @falcon.before()
    def on_post(self, req, res):
        res.status = falcon.HTTP_201
        res.body = json.dumps({
            'test': 'post'
        })

    # @falcon.before()
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = json.dumps({
            'test': 'get2'
        })
