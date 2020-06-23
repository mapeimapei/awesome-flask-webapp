#3-4【基于py3.x】如何将多个小字符串拼接成一个大的字符串

#1  迭代列表，连续使用“+” 操作依次拼接每个字符串

s1 = 'abcdef'
s2 = '1234455'

print( s1 + s2)
ss = str.__add__(s1,s2)
ss2 = s1.__add__(s2)
print(ss,ss2)





