# try except finally


def exe_try():
    try:
        f_read = open("../bobby.txt")
        print("code started")
        raise KeyError('sssss')
        return 1
    except KeyError as e:
        print(f"key error {e}")
        return 2
    else:
        print("other error")
        return 3
    finally:
        f_read.close()
        print("finally")
        return 4


# return 在try中的规则，如果finally中有return 则返回finally中。这里使用了栈的用法。

# 上下文管理器 with
class Sample():
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print("doing something")




if __name__ == "__main__":
#     result = exe_try()
#     print(result)
    with Sample() as sample:
        sample.do_something()