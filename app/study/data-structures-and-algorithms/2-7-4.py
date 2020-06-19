# 2-7【基于py3.x】如何实现用户的历史记录功能最多n条
from random import randint
from collections import deque


# 使用容量为n的队列存储历史记录
# 使用标准库collections 中的deque,它是一个双端循环队列
# 使用pickle 模块将历史记录存储到硬盘，以便下次启动使用

def guess(n, k):
    if n == k:
        print("猜对了，这个数字是%d." % k)
    if n < k:
        print('猜大了，比%d小。' % k)
    elif n > k:
        print('猜小了，比%d大。' % k)
    return False


def main():
    n = randint(1, 100)
    i = 1
    hq = deque([], 5)
    while True:
        line = input('[%d] 请输入一个数字：' % i)
        if line.isdigit():
            k = int(line)
            hq.append(k)
            i += 1
            if guess(n, k):
                break
        elif line == "quit":
            break
        elif line == "h?":
            print(list(hq))


if __name__ == "__main__":
    main()
