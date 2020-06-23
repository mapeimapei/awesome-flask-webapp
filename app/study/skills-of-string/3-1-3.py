#3-1【基于py3.x】如何拆分含有多种分隔符的字符串

#1 连续使用是str.split() 方法，每次处理一种分隔符号。

from functools import reduce

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

ss = reduce(lambda l,sep: sum( map(lambda ss:ss.split(sep),l),[]),',;|\t',[s])

print(ss)




