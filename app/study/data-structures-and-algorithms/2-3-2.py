# 2-3【基于py3.x】如何根据字典中值的大小对字典中的项排序

# 方案2 传递sorted 函数的key 参数

from random import randint

d = {k: randint(60, 100) for k in 'abcdefgh'}
print(d.items())

p = sorted(d.items(),key = lambda item:item[1],reverse=True)

#print(p)
#
# ll3 = list(enumerate(p,1))
#
# print(ll3)

for i,(k,v) in enumerate(p,1):
    #print(i,k,v)
    d[k] = (i,v)

print(d)

dd = {k:(i,v) for i,(k,v) in enumerate(p,1)}

print(dd)










