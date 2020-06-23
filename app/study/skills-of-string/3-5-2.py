#3-5【基于py3.x】如何对字符串进行左右居中对齐

#方法一，使用字符串的str.ljust(),str.rjust(),str.center() 进行左，右，居中对齐

#方法二，使用format() 方法，传递类似 "<20",">20","^20"参数完成同样任务

d = {'loDist':100.0,'SmallCull':0.04,'mapei':500.0}

w = max(map(len,d.keys()))
print(w)

for k,v in d.items():

    print(k.ljust(w),":",v)









