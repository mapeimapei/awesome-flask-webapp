# 列表生成式（列表推导式）
# 1 提取出1-20之间的奇数

odd_list = [x for x in range(21) if x % 2 == 1]
print(odd_list)


# 2 逻辑复杂的情况
def handle_item(item):
    return item * item


list2 = [handle_item(x) for x in range(21) if x % 2 == 1]

# 列表生成式的性能高于列表操作

print(list2)

#生成器表达式
odd_gen = (x for x in range(21) if x % 2 == 1)
print(odd_gen)
print(type(odd_gen)) #<class 'generator'>
odd_list = list(odd_gen)
print(type(odd_list))
for item in odd_list:
    print( item,end=",")

print("#####################")
#字典推导式

my_dict = {"bobby1":22,"boddy2":23,"imooc,com":5}

reverse_dict = {value:key for key,value in my_dict.items()}

print(reverse_dict)

#集合推导式
#my_set = set(my_dict.keys())
my_set = {key for key,value in my_dict.items()}
print(my_set)






