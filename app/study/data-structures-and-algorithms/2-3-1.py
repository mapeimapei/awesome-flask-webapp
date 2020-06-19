# 2-3【基于py3.x】如何根据字典中值的大小对字典中的项排序

# 1 将字典中的项转化为（值，键）元组。（列表解析或zip）

from random import randint

d = {k: randint(60, 100) for k in 'abcdefgh'}
print(d)

l = [(v, k) for k, v in d.items()]

l2 = sorted(l, reverse=True)
print(l2)

# 2 zip 函数
ll = list(zip([1, 2, 3], [4, 5, 6]))
print(ll)

ll2 = list(zip(d.values(), d.keys()))
print(ll2)

ll3 = sorted(ll2, reverse=True)
print(ll3)
