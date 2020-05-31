from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.models.base import Base


class TestCCCCCC(Base):
    __tablename__ = 'test1'
    id = Column(Integer, primary_key=True)
    test = Column(Integer, default=1)


class Test1():
    test = 0


cc = (i for i in range(10))
print(type(cc))
print(tuple(cc))

print("aa {0}".format("sss"))

print("aa %s,%10.2f" % ("ssss",222))
print(date(1970,1,10))
