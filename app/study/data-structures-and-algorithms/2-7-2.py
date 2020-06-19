# 2-7【基于py3.x】如何实现用户的历史记录功能最多n条
from random import randint
from collections import deque

# 使用容量为n的队列存储历史记录
# 使用标准库collections 中的deque,它是一个双端循环队列
# 双端队列，队列两边都可以入队 出队

q = deque([], 5)
# q.append()
# q.appendleft()
# q.pop()
# q.popleft()
q.append(1)
q.append(11)
q.append(111)
q.append(1111)
q.append(1111)
print(q)  # deque([1, 11, 111, 1111, 1111], maxlen=5)
q.append(6)

print(q)  # deque([11, 111, 1111, 1111, 6], maxlen=5)
