'''
abc 抽象基类
我们去检查某个类是否有某种方法
'''


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['bobby1', 'bobby2'])
print(hasattr(com, '__len__'))

# 我们在某种情况之下希望判定某个对象的类型
from collections.abc import Sized

isinstance(com, Sized)

# 我们需要强制某个子类必须实现某个方法
# 实现了一个web框架，集成cache(redis,cache,memorychache)
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 如何去模拟一个抽象基类呢？


import abc

class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self,key):
        pass
    @abc.abstractmethod
    def set(self,key,value):
        pass

class RedisCache(CacheBase):
    def get(self,key):
        pass

    def set(self,key,value):
        pass



redis_cache = RedisCache()




# class CacheBase:
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError
#
#
# class RedisCache(CacheBase):
#     def set(self, key, value):
#         pass
#
#
# redis_cache = RedisCache()
# redis_cache.set('key', 'value')
