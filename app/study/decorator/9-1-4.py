#9-1【基于py3.x】如何使用函数装饰器

#定义装饰器函数，用它来生成一个在原函数基础添加了新功能的函数，替代原函数

def memo(func):
    cache = {}
    def wrap(*args):
        res = cache.get(args)
        if not res:
           res = cache[args] = func(*args)

        return res

    return wrap



# 斐波那契数列 1,1,2,3,5,8,13,21,34
#求数列第n项的值?
@memo
def fibonacci(n):
    if n<=1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#fibonacci = memo(fibonacci)

print(fibonacci(50))




# 走楼梯问题
# 有100阶楼梯，一个人每次可以迈1-3阶，一共有多少种走法
@memo
def climb(n,steps):
    count = 0
    if n == 0:
        count = 1
    elif n> 0:
        for step in steps:
            count += climb(n-step,steps)
    return count

#climb = memo(climb)

print(climb(100,(1,2,3)))










