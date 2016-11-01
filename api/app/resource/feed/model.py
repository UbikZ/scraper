from sqlalchemy import Column, Integer, Sequence, String


class FeedModel(object):
    __tablename__ = 'feed_model'
    id = Column(Integer, Sequence('feed_id_seq'), primary_key=True)
    label = Column(String, nullable=False)
    url = Column(String, nullable=False)
