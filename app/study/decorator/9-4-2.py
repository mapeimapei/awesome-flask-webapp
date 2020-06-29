# 9-4【基于py3.x】如何实现属性可修改的函数装饰器

import time
import logging


def warn_timeout(timeout):
    def decorator(func):
        def wrap(*args, **kwargs):
            t0 = time.time()
            res = func(*args, **kwargs)
            used = time.time() - t0
            if used > timeout:
                logging.warning("%s:%s > %s", func.__name__, used, timeout)

            return res

        def set_timeout(new_timeout):
            nonlocal timeout
            timeout = new_timeout

        wrap.set_timeout = set_timeout

        return wrap

    return decorator


import random


@warn_timeout(1.5)
def f(i):
    print('in f [%s] ' % i)
    while random.randint(0, 1):
        time.sleep(0.6)


f.set_timeout(1)
for i in range(30):
    f(i)
