# array,deque
# 数组

import array
#array 和list 的一个重要区别，array只能存放指定的数据类型
aa = [3,4,5]
my_array = array.array('i')
my_array.append(1)
#my_array.append("abc")
my_array.fromlist(aa)

print(my_array)

