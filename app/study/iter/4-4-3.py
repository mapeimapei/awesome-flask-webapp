# 4-4【基于py3.x】如何进行反向迭代以及如何实现反向迭代

from collections.abc import Iterable
from functools import reduce
from decimal import Decimal
print(Decimal('0.2'))
print(type(Decimal('0.2')))

rr = reduce(Decimal.__add__,[Decimal('0.2')*50])

print(rr)