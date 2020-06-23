#3-1【基于py3.x】如何拆分含有多种分隔符的字符串

#2 使用正则表达式的 re.split() 方法。（推荐）
import  re

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

rr = re.split('[;,|\t]+',s)

print(rr)




