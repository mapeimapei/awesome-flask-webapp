#3-5【基于py3.x】如何对字符串进行左右居中对齐

#方法一，使用字符串的str.ljust(),str.rjust(),str.center() 进行左，右，居中对齐

#方法二，使用format() 方法，传递类似 "<20",">20","^20"参数完成同样任务

s = "abc"
s.ljust(10)
print(len(s.ljust(10)))

sss = s.ljust(10,"*")
print(sss)

sss = s.rjust(10,"*")
print(sss)

sss = s.center(10,"*")
print(sss)

#############

print(format(s,'<10'))
print(format(s,'>10'))
print(format(s,'<10'))
print(format(s,'^10'))

print(format(s,'*^10'))

n=5

n2 = n.__format__('>11')
print(n2)
n3 = format(n,"+")
print(n3)

print(format(-123,"+"))
print(format(-123,">+10"))
print(format(-123,"=+10"))
print(format(-123,"0=+10"))
print(format(546,"0=+10"))
