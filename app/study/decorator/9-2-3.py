#9-2【基于py3.x】如何为被装饰的函数保存元数据

from functools import update_wrapper,wraps

def my_decorator(func):
    @wraps(func)
    def wrap(*args,**kwargs):
        '''某功能包裹函数'''

        #此处实现某种功能
        #...

        return func(*args,**kwargs)
    # wrap.__name__ = func.__name__
    # wrap.__doc__ = func.__doc__
    #update_wrapper(wrap,func)
    return wrap

@my_decorator
def xxx_func(a,b):

    '''
    xxx_func 函数文档：
    :param a:
    :param b:
    :return:
    '''
    pass

print(xxx_func.__name__)
print(xxx_func.__doc__)




