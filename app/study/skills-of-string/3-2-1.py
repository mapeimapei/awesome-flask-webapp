#3-2【基于py3.x】如何判断字符串a是否以字符串b开头或结尾

#使用str.startswith() 和 str.endswith() 方法
#(注意：多个匹配时参数使用元组)

fn = 'aaa.py'

s = fn.endswith('.py')
s2 = fn.endswith('.py1')
print(s,s2)

s3 = fn.endswith( ('.py','.sh') )
print(s3)

import os

d = os.listdir('.')
print(d)

s= os.stat('3-1-1.py')
print(s.st_mode)
print(oct(s.st_mode))

#os.chmod('3-1-1.py',s.st_mode | 0o100)

import  stat
print(stat.S_IXUSR)


# for fn in os.listdir():
#     if fn.endswith(('.py','.sh')):
#         fs = os.stat(fn)
#         os.chmod(fn,fs.st_mode | stat.S_IXUSR)









