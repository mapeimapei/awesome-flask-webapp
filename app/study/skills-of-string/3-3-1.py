#3-3【基于py3.x】如何调整字符串中文本的格式

'''
使用正则表达式 re.sub() 方法做字符串替换，利用正则表达式的捕获组，
捕获每个部分内容，在替换字符串中调整各个捕获组的顺序
'''

f = open('WindowsUpdate.log', encoding="utf8")
log = f.read()

print(log)

import  re
#re.sub(p,r,s)

ss = re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)

print(ss)


ss2 = re.sub(r'(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})',r'\g<m>/\g<d>/\g<y>',log)

print(ss2)












