"""用户ORM模型库"""
import time, logging, uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, SmallInteger, text
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.sql import func

from app.models import Base

logging.basicConfig(level=logging.DEBUG)
__author__ = "带土"


class User(Base):
    __tablename__ = 'user1'
    id = Column(String(50), primary_key=True, nullable=True)
    email = Column(String(50), unique=True, nullable=True, index=True)
    _passwd = Column('passwd', String(50))
    admin = Column(SmallInteger, server_default=text('0'))
    name = Column(String(24), nullable=False)
    image = Column(String(200), server_default="about:blank")
    address = Column(String(200))
    tel = Column(String(18), unique=True)


    @property
    def passwd(self):
        return self._passwd

    @passwd.setter
    def passwd(self, raw):
        self._passwd = generate_password_hash(raw)
