from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.models import Base


class TestCCCCCC(Base):
    __tablename__ = 'test1'
    id = Column(Integer, primary_key=True)
    test = Column(Integer, default=1)


class Test1():
    test = 0
