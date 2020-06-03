#python中的垃圾回收的算法是采用引用计数

a = 1
b = a

del a

a = object()
b =a
del a
print(b)
print(a)

