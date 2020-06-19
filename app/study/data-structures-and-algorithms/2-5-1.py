# 2-5【基于py3.x】如何快速找到多个字典中的公共键key

from random import randint, sample

d1 = {k: randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
d2 = {k: randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
d3 = {k: randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
print(d1, d2, d3)

# for k in d1:
#     if k in d2 and k in d3:
#         print(k)

l = [k for k in d1 if k in d2 and k in d3]

print(l)

dl = [d1,d2,d3]
ll = [k for k in dl[0] if all(map(lambda d: k in d,dl[1:]))]
print(ll)













