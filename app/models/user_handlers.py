"""定义基类"""
import time, logging

logging.basicConfig(level=logging.DEBUG)
from sqlalchemy import text
from app.models.base import Base

__author__ = "带土"


class User(Base):
    def __init__(self):
        super().__init__()

    # 插入注册用户数据
    def insert_register_data(self, args):
        sql = 'insert into users ' \
              '(id,email,passwd,admin,name,image,created_at,address,tel)' \
              ' VALUES (%(id)s,%(email)s,%(passwd)s,%(admin)s,%(name)s,%(image)s,%(created_at)s,%(address)s,%(tel)s)'
        affectedcount = 0
        try:
            cursor = self.engine.execute(sql, args)
            self.session.commit()
            affectedcount = cursor.rowcount
            logging.info("影响的数据行数{0}".format(affectedcount))
            cursor.close()
        except Exception as e:
            print(e)
        finally:
            # cursor.close()
            pass

        return affectedcount
