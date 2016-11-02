from sqlalchemy import Column, Integer, Sequence, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    token = Column(String(255), nullable=False)
    is_enabled = Column(Boolean, nullable=False, default=True)
