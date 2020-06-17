# 生成器函数，函数里只要有yield关键字

def gen_func():
    yield 1
    yield 2
    yield 3


# 惰性求值，延迟求值提供了可能

# 斐波拉契 1 1 2 3 5 8

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


print(fib(11))


def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list


print(fib2(11))



def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1

for data in gen_fib(11):
    print(data,end=",")


def func():
    return 1


if __name__ == "__main__":
    # 生成器对象，python遍历字节码的时候产出了，
    gen = gen_func()

    for value in gen:
        print(value)

    # re = func()
    # pass
