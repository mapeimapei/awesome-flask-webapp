# 4-6【基于py3.x】如何在一个for语句中迭代多个可迭代对象

'''
1(并行) 某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，同时
迭代三个列表，计算每个学生的总分

2(串行) 某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，
依次迭代每个列表，统计全学年成绩高于90分的人数

'''

# 串行，使用标准库中的itertools.chain，它能将多个可迭代对象连接

from random import randint
from itertools import chain

s = 'abc;123|xyz;678|feafd\tjaef'

from functools import reduce

ss = list(reduce(lambda it_s,sep:chain( *map(lambda ss:ss.split(sep),it_s)),';|\t',[s]))


print(ss)










