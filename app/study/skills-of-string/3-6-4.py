#3-6【基于py3.x】如何去掉字符串中不需要的字符

# 4 字符串的translate() 方法，可以同时删除多种不同字符

s = "abc1234zyz"

ss = s.translate({ord('a') : "X",ord('b') : "Y"})
print(ss)

d = s.maketrans('abcxyz',"XYZABC")
print(d)

ss = s.translate(d)

print(ss)

ss = s.translate({ord('a') : None})

print(ss)