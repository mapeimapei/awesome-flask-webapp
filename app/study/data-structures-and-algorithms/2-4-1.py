#2-4【基于py3.x】如何统计序列中元素的频度

#方案1，将序列转化为字典{元素：频度}，根据字典中的值排序

from random import randint
data = [randint(0,20) for _ in range(30)]
print(data)

d = dict.fromkeys(data,0)
print(d)

for x in data:
    d[x] += 1

print(d)

#s = sorted([(v,k) for k,v in d.items()],reverse=True)
s = sorted(((v,k) for k,v in d.items()),reverse=True)
print(s)

###########################
import  heapq

c = heapq.nlargest(3,((v,k) for k,v in d.items()))

print(c)





















