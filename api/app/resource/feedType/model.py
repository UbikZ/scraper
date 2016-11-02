from sqlalchemy import Column, Integer, Sequence, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FeedTypeModel(Base):
    __tablename__ = 'feed_type'
    id = Column(Integer, Sequence('feed_id_type_seq'), primary_key=True)
    label = Column(String(100), nullable=False)
    url_regexp = Column(String(255), nullable=False)
    content_regexp = Column(String(255), nullable=False)
    is_enabled = Column(Boolean, nullable=False, default=True)
