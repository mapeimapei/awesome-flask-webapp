# 2-2【基于py3.x】如何为元组中的每个元素命名提高程序可读性
s = ('jim', 16, 'male', 'jim8721@gmail.com')

from collections import namedtuple

Student = namedtuple('Student',['name','age','sex','email'])

s2 = Student('jim', 16, 'male', 'jim8721@gmail.com')

print(s2)

print(isinstance(s2,tuple))

#print(s2[1])
print(s2.name)