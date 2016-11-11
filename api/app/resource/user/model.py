from sqlalchemy import Column, Integer, Sequence, String, Boolean, CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(100), nullable=False, index=True)
    email = Column(String(255), nullable=True)
    token = Column(String(255), nullable=False)
    is_enabled = Column(Boolean, nullable=False, index=True, default=True)

    __table_args__ = (
        UniqueConstraint('username', name='c_unique_user_username'),
        CheckConstraint('email ~* \'^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$\'',
                        name='c_check_user_email'),
    )
