"""定义基类"""
from ..secure import SQLALCHEMY_DATABASE_URI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from datetime import datetime
from contextlib import contextmanager
from sqlalchemy import Column, Integer, SmallInteger
from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery

__author__ = "带土"

__all__ = ['db', 'Base','Base2']


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, throw=True):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            current_app.logger.exception('%r' % e)
            if throw:
                raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


# class BaseMixin(object):
#     def __getitem__(self, key):
#         return getattr(self, key)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)


class BaseNoCreateTime(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)


class Base2(object):
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
