# __getattr__, __gerattribure__
#__getattr__、__getattribute__魔法函数
#__gerattr__ 就是在查找不到属性的时候调用
from datetime import date
class User:
    def __init__(self, info={}):
        self.info = info

    def __getattr__(self,item):
        # print("not find attr")
        # return "not find attr"
        return self.info[item]

    # def __getattribute__(self, item):
    #     print(item)
    #     return "bobby"


if __name__ == "__main__":
    user = User( info={"company_name":"imooc","name":"bobby"})
    print(user.name)
    #print(user.test)





