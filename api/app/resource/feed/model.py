from sqlalchemy import Column, Integer, Sequence, String, Boolean, CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FeedModel(Base):
    __tablename__ = 'feed'

    id = Column(Integer, Sequence('seq_feed_id'), primary_key=True)
    ref_key = Column(String(100), nullable=False, index=True)
    url = Column(String(255), nullable=False)
    is_enabled = Column(Boolean, default=False, index=True)

    __table_args__ = (
        UniqueConstraint('ref_key', name='c_unique_feed_refKey'),
        CheckConstraint('url ~* \'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$\'',
                        name='c_check_feed_url'),
    )
