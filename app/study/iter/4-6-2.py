# 4-6【基于py3.x】如何在一个for语句中迭代多个可迭代对象

'''
1(并行) 某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，同时
迭代三个列表，计算每个学生的总分

2(串行) 某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，
依次迭代每个列表，统计全学年成绩高于90分的人数

'''

# 并行 使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组

from random import randint

chinese = [randint(60, 100) for _ in range(20)]
math = [randint(60, 100) for _ in range(20)]
english = [randint(60, 100) for _ in range(20)]

m = map(lambda *args:args,chinese,math,english)
print(list(m))
print(list(zip(chinese,math,english)))
