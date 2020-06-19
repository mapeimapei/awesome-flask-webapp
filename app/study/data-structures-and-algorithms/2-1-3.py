#py3.x】如何在列表字典集合中根据条件筛选数据
from random import randint

d = {'student%d' % i: randint(50, 100) for i in range(1, 21)}
print(d)

d1 = {k:v for k,v in d.items() if v >= 90}
print(d1)

g = filter(lambda item:item[1] >=90 ,d.items())

print(dict(g))