class DatabaseHandler(object):
    def __init__(self, db=None):
        self.db = db

    def process_request(self, req, res):
        req.context['db'] = self.db
