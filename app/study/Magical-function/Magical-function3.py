'''
 __开始  __结束的方法都是魔法函数，魔法函数很多。。
'''


class Nums(object):
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


my_num = Nums(-1)
print(abs(my_num))


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        re_vector = MyVector(self.x + other.x, self.y + other.y)
        return re_vector

    def __str__(self):
        return "x:{x},y:{y}".format(x=self.x, y=self.y)


first_vec = MyVector(1, 2)
second_vec = MyVector(2, 3)

print(first_vec + second_vec)
