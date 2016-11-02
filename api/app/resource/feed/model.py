from sqlalchemy import Column, Integer, Sequence, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FeedModel(Base):
    __tablename__ = 'feed'
    id = Column(Integer, Sequence('feed_id_seq'), primary_key=True)
    label = Column(String(100), nullable=False)
    url = Column(String(255), nullable=False)
    is_enabled = Column(Boolean, default=False)
