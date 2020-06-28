# 4-4【基于py3.x】如何进行反向迭代以及如何实现反向迭代

from collections.abc import Iterable

l = [1,2,3,4,5]

# l.reverse()
# print(l)

#print(l[::-1])

# l2 = reversed(l)
# print(l2)

for x in reversed(l):
    print(x)




