#私有属性
from class_method import Date

class User(Date):
    def __init__(self,birthday):
        self.__birthay = birthday

    def get_age(self):
        return 2020 - self.__birthay.year

if __name__=="__main__":
    user = User(Date(1984,11,12))
    print(user._User__birthay)
    print(user.get_age())



