#9-1【基于py3.x】如何使用函数装饰器

# 斐波那契数列 1,1,2,3,5,8,13,21,34
#求数列第n项的值?
def fibonacci(n):
    if n<=1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


#f = fibonacci(50)
#print(f)

# 走楼梯问题
# 有100阶楼梯，一个人每次可以迈1-3阶，一共有多少种走法

def climb(n,steps):
    count = 0
    if n == 0:
        count = 1
    elif n> 0:
        for step in steps:
            count += climb(n-step,steps)
    return count











