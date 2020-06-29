#9-1【基于py3.x】如何使用函数装饰器

cache = {}

# 斐波那契数列 1,1,2,3,5,8,13,21,34
#求数列第n项的值?
def fibonacci(n):

    res = cache.get(n)
    if res:
        return res

    if n<=1:
        return 1
    res = cache[n] =  fibonacci(n-1) + fibonacci(n-2)
    return  res

print(fibonacci(50))

