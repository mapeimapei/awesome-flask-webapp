#2-1【基于py3.x】如何在列表字典集合中根据条件筛选数据
from random import randint

s = {randint(0,20) for _ in range(1,21)}

print(s)

s2 = { x for x in s if x%3 == 0}

print(s2)

s3 = filter(lambda x:x%3==0,s)

print(set(s3))