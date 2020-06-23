#3-1【基于py3.x】如何拆分含有多种分隔符的字符串

#1 连续使用是str.split() 方法，每次处理一种分隔符号。

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

def my_split(s,seps):
    res = [s]
    for sep in seps:
        t = []
        list(map(lambda ss:t.extend(ss.split(sep)),res))
        res = t

    return res

res = my_split(s,',;|\t')

print(res)







