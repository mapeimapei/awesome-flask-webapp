#4-3【基于py3.x】如何使用生成器函数实现可迭代对象

from collections.abc import Iterable,Iterator

#将该类的 __iter__方法实现成生成器函数，每次yield返回一个素数


def f():
    print('in f 1')
    yield 1
    print('in f 2')
    yield 2
    print('in f 3')
    yield 3

print( f())
g = f()

print( isinstance(g,Iterator))
print( isinstance(g,Iterable))

print(iter(g) is g)


print(next(g))
print(next(g))
print(next(g))

#next(g)


