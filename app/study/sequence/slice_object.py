'''
手动实现可切片的对象
'''
import numbers


class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

        return self.staffs[item]

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ['bobby1', 'imooc', 'bobby2', 'bobby3']
group = Group(company_name="imooc", group_name='user', staffs=staffs)

sub_group = group[:2]
group = group[0]

reversed(sub_group)

for user in sub_group:
    print(user)

print(len(sub_group))
print(group)
if "bobby1" in group:
    print("yes")
