'''
定义:如果走起路来像鸭子，叫起来也像鸭子，那么它就是鸭子（If it walks like a duck and quacks like a duck, it must be a duck）

鸭子类型是编程语言中动态类型语言中的一种设计风格，一个对象的特征不是由父类决定，而是通过对象的方法决定的。
鸭子类型通常得益于不测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用。
'''


class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a dog")


class Duck(object):
    def say(self):
        print("i am a duck")


animal = Cat()
animal.say()
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


class Animal:
    def say(self):
        print('i am a animal')


class Cat(Animal):
    def __init__(self):
        pass


aa = Cat()
aa.say()

print("#############")

a = ['bobby1','bobby2']
b = ['bobby2','bobby']
name_tuple = ['bobby3','bobby4']
name_set = set()
name_set.add('bobby5')
name_set.add('bobby6')

a.extend(b)
a.extend(name_tuple)
a.extend(name_set)
print(a)

