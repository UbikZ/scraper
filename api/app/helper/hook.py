class Hook(object):
    @staticmethod
    def open_cursor(req, res, resource, params):
        db = req.context['db']
        resource.db = db
        resource.cursor = db.cursor()

    @staticmethod
    def close_cursor(req, res, resource):
        resource.cursor.close()
