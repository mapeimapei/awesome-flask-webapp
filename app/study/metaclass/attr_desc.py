from datetime import date, datetime
import numbers


# 属性描述符和属性查找过程

class IntField:
    #数据描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("Int value need")

        if value < 0:
            raise ValueError("positive value need")

        self.value = value

    def __delete__(self, instance):
        pass

class NonDataIntField:
    #非数据属性描述符
    def __get__(self, instance, owner):
        return self.value

class User:
    age = IntField()


#
# class User:
#     def __init__(self, name, email,birthday):
#         self.name = name
#         self.email = email
#         self.birthday = birthday
#         self._age = 0 # 不想对外暴露
#
#     # def get_age(self):
#     #     return datetime.now().year - self.birthday.year
#
#     @property
#     def age(self):
#         return datetime.now().year - self.birthday.year
#
#     @age.setter
#     def age(self,value):
#         self._age = value


if __name__ == "__main__":
    user = User()
    user.age = 30
    user.age = -1
    print(user.age)
    # user = User("bobby", date(year=1987, month=1, day=1))
    # user.age = 30
    # print(user._age)
    # print('in {} file'.format(__file__))
