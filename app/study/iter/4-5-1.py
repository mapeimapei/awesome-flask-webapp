# 4-5【基于py3.x】如何对迭代器做切片操作

from collections.abc import Iterable

f = open('../skills-of-string/WindowsUpdate.log', encoding='utf8')

l = list(range(10))
print(l[2:9])

print(l[3])
print(l.__getitem__(3))
print(l.__getitem__(slice(2,4)))



