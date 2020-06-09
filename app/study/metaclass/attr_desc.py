from datetime import date, datetime
import numbers


# 属性描述符和属性查找过程
'''
如果user是某个类的实例，那么user.age(以及等价的getatter(user,"age"))
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出AttributeError的时候就会调用到__getattr__,
而对于描述符(__get__)的调用，则是发生在__getattribute__内部的。
user = User(),那么user.age顺序如下：
1，如果“age”是出现在User或者基类的__dict__中，且age是data descriptor，那么调用其__get__方法，否则
2，如果“age”出现在obj（user）的__dict__中，那么直接返回obj.__dict__['age'],否则
3，如果“age”出现在User或者其基类的__dict__中
3.1 如果age是non-data descriptor,那么调用其__get__方法，否则
3.2 返回__dict__['age']
4 如果User有__getattr__ 方法，调用__getattr__方法，否则
5 抛出AttributeError
'''







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
    #age = NonDataIntField()

if __name__ == "__main__":
    user = User()
    user.age = 30
    #user.age = -1
    user.__dict__["age"] = "abc"
    print(user.__dict__)
    print(user.age)
    # user = User("bobby", date(year=1987, month=1, day=1))
    # user.age = 30
    # print(user._age)
    # print('in {} file'.format(__file__))
