# 4-3【基于py3.x】如何使用生成器函数实现可迭代对象

from collections.abc import Iterable


# 将该类的 __iter__方法实现成生成器函数，每次yield返回一个素数

class PrimeNumers(Iterable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        for k in range(self.a, self.b + 1):
            if self.is_prime(k):
                yield k

    def is_prime(self, k):
        # if k < 2:
        #     return  False

        # for x in range(2,k):
        #     if k%x == 0:
        #         return False

        return False if k < 2 else all(map(lambda x: k % x, range(2, k)))


pn = PrimeNumers(1,30)

for i in pn:
    print(i)