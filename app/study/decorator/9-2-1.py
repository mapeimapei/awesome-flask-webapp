#9-2【基于py3.x】如何为被装饰的函数保存元数据

def f(a:int,b:int,c=1) -> int:
    '''function f'''
    pass

print(f.__name__)
print(f.__module__)
print(f.__doc__)
print(f.__annotations__)
print(f.__defaults__)


#闭包

def ff(a):
    return lambda n:a**n

g = ff(3)

print(g(4))





