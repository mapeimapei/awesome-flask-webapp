#3-6【基于py3.x】如何去掉字符串中不需要的字符

#1 字符串strip(),lstrip(),rstrip()方法去掉字符串两端的字符
s = "  nihao@qq.com  "

print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = " \t nihoa@qq.com  \t  "
print(s.strip())


s = "=+-==nihoa@qq.com=,+-="
print(s.strip('=+-,')) #nihoa@qq.com






