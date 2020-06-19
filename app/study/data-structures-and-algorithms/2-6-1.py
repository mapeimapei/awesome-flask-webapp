#2-6【基于py3.x】如何让字典保持有序
d = {}
d["cc"] = 1
d["c"] = 1
d["b"] = 2
d["a"] = 3
d["nihao"] = 3
d["v"] = 3
d["z"] = 3
print(d.keys())
print(list(iter(d)))

#python3.6中 字典已经是一个有序字典了
