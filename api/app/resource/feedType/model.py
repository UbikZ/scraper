from sqlalchemy import Column, Integer, Sequence, String, Boolean, UniqueConstraint, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FeedTypeModel(Base):
    __tablename__ = 'feed_type'

    id = Column(Integer, Sequence('seq_feedType_id'), primary_key=True)
    ref_key = Column(String(100), nullable=False, index=True)
    label = Column(String(100), nullable=False)
    url_regexp = Column(String(255), nullable=False)
    content_regexp = Column(String(255), nullable=False)
    is_enabled = Column(Boolean, nullable=False, index=True, default=True)

    __table_args__ = (
        UniqueConstraint('ref_key', name='c_unique_feedType_refKey'),
    )
