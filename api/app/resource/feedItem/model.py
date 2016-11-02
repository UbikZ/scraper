from sqlalchemy import Column, Integer, Sequence, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FeedItemModel(Base):
    __tablename__ = 'feed_item'
    id = Column(Integer, Sequence('feed_id_item_seq'), primary_key=True)
    feed_id = Column(Integer, ForeignKey('feed.id', name='fk_feedItem_parent_feedId'))
    feed_type = Column(Integer, ForeignKey('feed_type.id', name='fk_feedItem_parent_feedType'))
    url = Column(String(255), nullable=False, unique=True)
    title = Column(String(100), nullable=False)
    tags = Column(String(255), nullable=True)
    date = Column(DateTime, nullable=False, default=func.now())
    is_enabled = Column(Boolean, nullable=False, default=True)
    is_viewed = Column(Boolean, nullable=False, default=False)
    is_approved = Column(Boolean, nullable=False, default=False)
    is_reposted = Column(Boolean, nullable=False, default=False)
    is_sent = Column(Boolean, nullable=False, default=False)
