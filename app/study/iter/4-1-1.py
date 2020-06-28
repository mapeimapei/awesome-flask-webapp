#4-1【基于py3.x】如何实现可迭代对象和迭代器对象1
from collections.abc import Iterator, Iterable

l = [1, 2, 3, 4, 5, 6, 7]
for x in l:
    print(x)

print(isinstance(l, Iterable))
print(issubclass(list, Iterable))
print(issubclass(dict, Iterable))
print(issubclass(str, Iterable))
print(issubclass(int, Iterable))

print(iter(l))
print(l.__iter__())

it = iter(l)
print(next(it))

for x in it:
    print(x)


print( isinstance(it,Iterable))
print( isinstance(it,Iterator))
print( it.__iter__())
print( it.__iter__() is it)






