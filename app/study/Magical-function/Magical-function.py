'''
 __开始  __结束的方法都是魔法函数，魔法函数很多。。
'''

class Company(object):
    def __init__(self, enployee_list):
        self.employee = enployee_list

    def __getitem__(self, item):
        print("1", item)
        return self.employee[item]


    def __len__(self):
        return len(self.employee)


company = Company(['tom', 'bob', 'jane'])

company1 = company[:2]
print(len(company))

for em in company1:
    print(em)

print(company)