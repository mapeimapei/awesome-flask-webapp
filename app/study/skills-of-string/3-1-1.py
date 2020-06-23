#3-1【基于py3.x】如何拆分含有多种分隔符的字符串

#1 连续使用是str.split() 方法，每次处理一种分隔符号。

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
ss= s.split(';')
print(ss)

ss2 = [ss.split('|') for ss in s.split(';')]
print(ss2)

mm =list( map(lambda ss: ss.split('|'),s.split(';')))
print(mm)

t = []

t.extend([1,2,3])
t.extend([4,5,6])
print(t)
##
tt = []
list(map(tt.extend,[ss.split('|') for ss in s.split(';')]))

print(tt)

##
cc = sum([ss.split('|') for ss in s.split(';')],[])

print(cc)







