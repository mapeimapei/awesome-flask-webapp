# 自省是通过一定的机制查询到对象的内部结构

from class_method import Date


class Person:
    '''
    人
    '''
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == "__main__":
    user = Student("慕课网")

    # 通过__dict__ 查询属性

    print(user.__dict__)
    user.__dict__["school_addren"] = "北京市"
    print(user.school_addren)
    print(Person.__dict__)
    print(user.name)

    print(dir(user))

    a = [1, 3]
    print(dir(a))
