#4-3【基于py3.x】如何使用生成器函数实现可迭代对象

from collections.abc import Iterable,Iterator

#将该类的 __iter__方法实现成生成器函数，每次yield返回一个素数

class XXX_Iterable(Iterable):
    def __iter__(self):
        yield 1
        yield 2
        yield 3

x = XXX_Iterable()

g = iter(x)

for x in g:
    print(x)







