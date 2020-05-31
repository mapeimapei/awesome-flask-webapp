# 尽量多的使用isinstance  少用 type
class A:
    pass

class B(A):
    pass

b = B()

print( isinstance(b,B))
print(isinstance(b,A))
print( type(b))
print( type(b) == B)
print( type(b) is B)
print( type(b) is A)
'''A
 ==  值是否相等
 is 是不是一个对象
'''













