# 2-2【基于py3.x】如何为元组中的每个元素命名提高程序可读性
s = ('jim', 16, 'male', 'jim8721@gmail.com')
t = (32, 'liushuo')
from enum import IntEnum


class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3


print(StudentEnum.NAME)
print(s[StudentEnum.NAME])

print(isinstance(StudentEnum.NAME,int))

print(StudentEnum.AGE == 1)












