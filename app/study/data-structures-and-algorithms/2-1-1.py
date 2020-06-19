#py3.x】如何在列表字典集合中根据条件筛选数据

data = [-1,2,3,-4,5]

res = []
for x in data:
    if x>=0:
        res.append(x)

print(res)


