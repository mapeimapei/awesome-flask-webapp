# 2-6【基于py3.x】如何让字典保持有序

from collections import OrderedDict

od = OrderedDict()
od["cc"] = 1
od["c"] = 1
od["b"] = 2
od["a"] = 3
od["nihao"] = 3
od["v"] = 3
od["z"] = 3
print(od.keys())
print(list(iter(od)))

players = list('abcdefgh')
from random import shuffle

shuffle(players)
print(players)

od2 = OrderedDict()
for i,p in enumerate( players,1):
    print(p)
    od2[p] = i

print(od2)

def query_by_name(d,name):
    return d[name]


aa = query_by_name(od2,'c')

print(aa)



from itertools import islice

ll = islice(range(10),3,6)
print(list(ll))
ll = islice(od2,3,6)
print(list(ll))

def query_by_order(d,a,b=None ):
    a -= 1
    if b is None:
        b = a + 1

    return list(islice(d,a,b))

cc = query_by_order(od2,3,5)

print(cc)