# 2-5【基于py3.x】如何快速找到多个字典中的公共键key

from random import randint, sample

d1 = {k: randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
d2 = {k: randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
d3 = {k: randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
print(d1, d2, d3)

dl = [d1,d2,d3]

# 利用集合（set）的交集操作
# 1 step1：使用字典的keys() 方法，得到一个字典的keys的集合
# step2 使用map函数，得到每个字典keys的集合
# step3 使用reduce函数，取所有字典的keys集合的交集

s1 = d1.keys()
s2 = d2.keys()

print(s1 & s2)

from functools import reduce

aa = reduce(lambda a,b:a*b,range(1,11))

print(aa)

# d1.keys() == dict.keys(d1)

l = list(map(dict.keys,dl))

print(l)

ss = reduce(lambda a,b:a&b,map(dict.keys,dl))

print(ss)



