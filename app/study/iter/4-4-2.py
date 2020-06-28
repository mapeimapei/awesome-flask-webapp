# 4-4【基于py3.x】如何进行反向迭代以及如何实现反向迭代

from collections.abc import Iterable
from decimal import Decimal


# Decimal('0.2')

# 实现反向迭代协议的 __reversed__ 方法，它返回一个反向迭代器


class FloatRange:
    def __init__(self, a, b, step):
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.step = Decimal(str(step))

    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield float(t)
            t += self.step

    def __reversed__(self):
        t = self.b
        while t >= self.a:
            yield float(t)
            t -= self.step


fr = FloatRange(3.0, 4.0, 0.2)

for x in fr:
    print(x)

print('-' * 20)
for x in reversed(fr):
    print(x)
