aList = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(aList[::])  # 返回包含原列表中所有元素的新列表
print(aList[::-1])  # 返回包含原列表中所有元素的逆序列表
print(aList[::2])  # 隔一个取一个，获取偶数位置的元素
print(aList[1::2])  # 隔一个取一个，获取奇数位的元素
print(aList[3:6])  # 指定切片开始和结束位置
aList[0:100]  # 切片结束位置大于列表长度时，从列表尾部截断
aList[100:]  # 切片开始位置大于列表长度时，返回空列表

aList[len(aList):] = "22"
aList[len(aList):] = [9]  # 在列表尾部增加元素

aList[:0] = [1, 2]  # 在列表头部插入元素

aList[3:3] = [4] #在列表中间位置插入元素
aList[:3] = [1,2,100,88,999] #替换列表元素，等号两边的列表长度相等

aList[3:] = [4,5,600] #等号两边的列表长度也可以不相等
print(aList)
aList[::2] = [0] *3 #隔一个修改一个
print(aList)

aList[::2] = ["a","b","v"] #隔一个修改一个
print(aList)
#aList[::2] = [1,2] #这个会失败，左侧切片不连续，等号两边列表的长度必须相等
aList[:3] = [] #删除列表中的前三个元素
print(aList)
#del aList[:3] #切片元素连续
print(aList)
del aList[::2] #切片元素不连续

print(aList)