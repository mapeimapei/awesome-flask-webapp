'''
 __开始  __结束的方法都是魔法函数，魔法函数很多。。
'''

class Company(object):
    def __init__(self, enployee_list):
        self.employee = enployee_list

    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return ','.join(self.employee)


company = Company(['tom', 'bob', 'jane'])

#company

#repr(company)
company.__repr__()
print(company)