"""定义基类"""
from ..secure import SQLALCHEMY_DATABASE_URI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

__author__ = "带土"


class Base(object):
    def __init__(self):
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URI,
            pool_size=10,
            pool_recycle=7200,
            pool_pre_ping=True,
            encoding='utf-8'
        )

    @property
    def session(self):
        session_factory = sessionmaker(bind=self.engine)
        return session_factory()


    @property
    def conn(self):
        conn2 = self.engine.raw_connection()
        return conn2

