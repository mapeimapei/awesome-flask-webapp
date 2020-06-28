# 4-5【基于py3.x】如何对迭代器做切片操作

from collections.abc import Iterable

f = open('../skills-of-string/WindowsUpdate.log', encoding='utf8')

# lines = f.readlines()
# print( lines[1:30])

# 使用 itertools.islice 它能返回一个迭代对象切片的生成器

from itertools import islice

for line in islice(f, 20 - 1, 30):
    print(line)
