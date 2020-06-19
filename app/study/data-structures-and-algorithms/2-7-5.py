# 2-7【基于py3.x】如何实现用户的历史记录功能最多n条
from random import randint
from collections import deque
import pickle

# 使用容量为n的队列存储历史记录
# 使用标准库collections 中的deque,它是一个双端循环队列
# 使用pickle 模块将历史记录存储到硬盘，以便下次启动使用

q = [1,2,3,5,7,8]
pickle.dump(q,open('save.pkl','wb'))

q2 = pickle.load(open('save.pkl','rb'))

print(q2)