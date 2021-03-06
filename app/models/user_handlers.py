"""用户模型库 这个文件已废弃"""
import time, logging, uuid

from sqlalchemy import text
from app.models.base import Base2

logging.basicConfig(level=logging.DEBUG)
__author__ = "带土"


class User(Base2):
    def __init__(self):
        super().__init__()

    # 获取登陆用户数据
    def get_user_data(self, args):
        sql = 'select user_id,name,address,tel from users where (name = :account or email=:account) And passwd = :passwd'
        print(f'sql:{sql}')
        fields = {}
        try:
            resultProxy = self.session.execute(text(sql), args)
            res_row = resultProxy.fetchone()
            print("res_row", res_row)
            if res_row:
                fields['id'] = res_row[0]
                fields['name'] = res_row[1]
                fields['address'] = res_row[2]
                fields['tel'] = res_row[3]
                fields['token'] = str('%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex))

        except Exception as e:
            print(e)
        finally:
            self.session.close()

        return fields

    # 插入注册用户数据
    def insert_register_data(self, args):
        sql = 'insert into users ' \
              '(id,email,passwd,admin,name,image,created_at,address,tel)' \
              ' VALUES (%(id)s,%(email)s,%(passwd)s,%(admin)s,%(name)s,%(image)s,%(created_at)s,%(address)s,%(tel)s)'
        affectedCount = 0
        try:
            cursor = self.engine.execute(sql, args)
            self.session.commit()
            affectedCount = cursor.rowcount
            logging.info(f"影响的数据行数{affectedCount}")
        except Exception as e:
            print(e)
        finally:
            self.session.close()
            pass

        return affectedCount
