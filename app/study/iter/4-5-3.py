# 4-5【基于py3.x】如何对迭代器做切片操作

from collections.abc import Iterable

f = open('../skills-of-string/WindowsUpdate.log', encoding='utf8')

# lines = f.readlines()
# print( lines[1:30])

# 使用 itertools.islice 它能返回一个迭代对象切片的生成器

from itertools import islice

def my_islice(iterable,start,end,step=1):
    tmp = 0
    for i,x in enumerate(iterable):
        if i>=end:
            break

        if i >=start:
            if tmp == 0:
                tmp = step
                yield x
            tmp -=1


l = list(my_islice(range(100,150),10,20,3))
print(l)
l2 = list(islice(range(100,150),10,20,3))
print(l2)





