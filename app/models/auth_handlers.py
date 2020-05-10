"""用户ORM模型库"""
import time, logging, uuid

from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, SmallInteger, text
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.util import next_id
from app.models import Base
from app import login_manager

logging.basicConfig(level=logging.DEBUG)
__author__ = "带土"


class User(Base):
    __tablename__ = 'users'
    _user_id = Column("user_id", String(50), nullable=False, primary_key=True)
    email = Column(String(50), unique=True, nullable=True, index=True)
    _passwd = Column('passwd', String(128), nullable=False)
    admin = Column(SmallInteger, server_default=text("0"))
    name = Column(String(24), nullable=False)
    image = Column(String(200), server_default="about:blank")
    address = Column(String(200))
    tel = Column(String(18), unique=True)

    def keys(self):
        return ['user_id', 'email', 'name', 'tel']

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, raw):
        self._user_id = next_id()

    @property
    def passwd(self):
        return self._passwd

    @passwd.setter
    def passwd(self, raw):
        self._passwd = generate_password_hash(raw)

    def check_password(self, row):
        print("check_password", row)
        return check_password_hash(self._passwd, row)

    def get_id(self):
        return self._user_id


@login_manager.user_loader
def get_user(uid):
    return User.query.get(str(uid))
