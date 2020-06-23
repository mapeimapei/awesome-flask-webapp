#3-6【基于py3.x】如何去掉字符串中不需要的字符

#3 字符串的replace() 方法或正则表达式re.sub()删除任意子串

s3 = "  avc sdf dsfdg "

s4 = s3.replace(" ","")
print(s4)


s3 = " \t \n avc \t sdf dsfdg \n "
import re
s4 = re.sub('[ \t\n]+',"",s3)
s5 = re.sub('\s+',"",s3)
print(s5)





