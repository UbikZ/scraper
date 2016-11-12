from sqlalchemy import Column, Integer, Sequence, String, Boolean, ForeignKey, DateTime, func, CheckConstraint, \
    UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FeedItemModel(Base):
    __tablename__ = 'feed_item'

    id = Column(Integer, Sequence('seq_feedItem_id'), primary_key=True)
    feed_id = Column(Integer, ForeignKey('feed.id', name='fk_feedItem_parent_feedId'))
    feed_type = Column(Integer, ForeignKey('feed_type.id', name='fk_feedItem_parent_feedType'))
    url = Column(String(255), nullable=False)
    hash = Column(String(42), nullable=False)
    title = Column(String(100), nullable=False)
    tags = Column(String(255), nullable=True)
    date = Column(DateTime, nullable=False, default=func.now())
    is_enabled = Column(Boolean, nullable=False, default=True, index=True)
    is_viewed = Column(Boolean, nullable=False, default=False, index=True)
    is_approved = Column(Boolean, nullable=False, default=False, index=True)
    is_reposted = Column(Boolean, nullable=False, default=False, index=True)
    is_sent = Column(Boolean, nullable=False, default=False, index=True)

    __table_args__ = (
        CheckConstraint('url ~* \'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$\'',
                        name='c_check_feedItem_url'),
        UniqueConstraint('url', name='c_unique_feedItem_url'),
        UniqueConstraint('hash', name='c_unique_feedItem_hash'),
    )
