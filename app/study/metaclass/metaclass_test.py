# 类也是对象，type创建类的类

def creat_class(name):
    if name == "user":
        class User:
            name = "user"
            def __str__(self):
                return "user"

        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


#type 动态创建类



def say(self):
    return "i am user"
    #return self.name


class BaseClass:
    def answer(self):
        return "i am baseclass"

#User = type("User",(),{"name":"user","say":say})


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        print("ccccccc")
        return  super().__new__(cls,*args, **kwargs)


#什么是元类，元类是创建类的类，对象<- class(对象) <- type
class User(metaclass=MetaClass):

    # def __new__(cls, *args, **kwargs):
    #     super().__new__(cls)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user11"




#python 中类的实例化过程，会首先寻找metaclass，通过metaclass去创建user类
#type去创建类对象，实例




if __name__ == "__main__":
    # MyClass = creat_class("user")
    # my_obj = MyClass()
    # print(type(my_obj))

    #User = type("User",(BaseClass,),{"name":"user","say":say})
    my_obj = User(name = "bobby")
    print(my_obj)
    #print( my_obj.name)
    #print(my_obj.say())
    #print(my_obj.answer())