"""用户ORM模型库"""
import time, logging, uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, SmallInteger, text
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.util import next_id
from app.models import Base
from app import login_manager

logging.basicConfig(level=logging.DEBUG)
__author__ = "带土"


class User(Base):
    __tablename__ = 'user1'
    _userid = Column("userid", String(50), nullable=False,primary_key=True)
    email = Column(String(50), unique=True, nullable=True, index=True)
    _passwd = Column('passwd', String(128), nullable=False)
    admin = Column(SmallInteger, server_default=text("0"))
    name = Column(String(24), nullable=False)
    image = Column(String(200), server_default="about:blank")
    address = Column(String(200))
    tel = Column(String(18), unique=True)

    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, raw):
        print("userid", raw)
        self._userid = next_id()

    @property
    def passwd(self):
        return self._passwd

    @passwd.setter
    def passwd(self, raw):
        print("fffffff", raw)
        self._passwd = generate_password_hash(raw)

    def check_password(self, row):
        return check_password_hash(self._passwd, row)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
