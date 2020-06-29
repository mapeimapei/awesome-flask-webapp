# 9-5【基于py3.x】如何在类中定义装饰器

import time
import logging

DEFAULT_FORMAT = '%(func_name)s -> %(call_time)s\t%(used_time)s\t%(call_n)s'


class CallInfo:
    def __init__(self, log_path, format_=DEFAULT_FORMAT, on_off=True):
        self.log = logging.getLogger(log_path)
        self.log.addHandler(logging.FileHandler(log_path))
        self.log.setLevel(logging.INFO)
        self.format = format_
        self.is_on = on_off

    # 装饰器方法
    def info(self, func):
        _call_n = 0

        def wrap(*args, **kwargs):
            func_name = func.__name__
            call_time = time.strftime('%x %X', time.localtime())
            t0 = time.time()
            res = func(*args, **kwargs)
            used_time = time.time() - t0
            nonlocal _call_n
            _call_n += 1
            call_n = _call_n
            if self.is_on:
                self.log.info(self.format % locals())
            return res

        return wrap

    def set_format(self, format_):
        self.format = format_

    def turn_on_off(self, on_off):
        self.is_on = on_off


# 测试代码
import random

ci1 = CallInfo('mylog1.log')
ci2 = CallInfo('mylog2.log')


@ci1.info
def f():
    sleep_time = random.randint(0, 6) * 0.1
    time.sleep(sleep_time)


@ci1.info
def g():
    sleep_time = random.randint(0, 8) * 0.1
    time.sleep(sleep_time)


@ci2.info
def h():
    sleep_time = random.randint(0, 7) * 0.1
    time.sleep(sleep_time)


for _ in range(30):
    random.choice([f, g, h])()

ci1.set_format('%(func_name)s -> %(call_time)s\t%(call_n)s')
for _ in range(30):
    random.choice([f, g])()


