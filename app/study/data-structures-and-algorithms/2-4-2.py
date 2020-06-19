#2-4【基于py3.x】如何统计序列中元素的频度

#方案2，使用标准库collection 中的Counter对象
from  collections import Counter
from random import randint
data = [randint(0,20) for _ in range(30)]
print(data)

c = Counter(data)

print(c)

cc = c.most_common(3)

print(cc)










