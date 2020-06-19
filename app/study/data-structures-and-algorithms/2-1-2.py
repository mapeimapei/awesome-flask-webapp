#py3.x】如何在列表字典集合中根据条件筛选数据
from random import randint

print( randint(-10,10))

l = [randint(-10,10) for _ in range(10)]

print(l)

ll = [ x for x in l if x>= 0]
print(ll)

ll3 = list(filter(lambda x:x>=0,l))
print(ll3)

