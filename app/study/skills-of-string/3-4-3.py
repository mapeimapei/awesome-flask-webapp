#3-4【基于py3.x】如何将多个小字符串拼接成一个大的字符串

#1  迭代列表，连续使用“+” 操作依次拼接每个字符串

l = ['<0112>',"32","<1024x768>","<b0>","<500.0>"]

sss = ''.join(l)
print(sss)


l2 = ['avc','ccc','sfx']

s = ':'.join(l2)
print(s)


