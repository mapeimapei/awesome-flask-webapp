#9-3【基于py3.x】如何定义带参数的装饰器
import inspect

def type_assert(*ty_args,**ty_kwargs):
    def decorator(func):
        #A...

        func_sig = inspect.signature(func)
        bind_type = func_sig.bind_partial(*ty_args,**ty_kwargs).arguments

        def wrap(*args,**kwargs):
            #B...

            for name,obj in func_sig.bind(*args, **kwargs).arguments.items():
                type_ = bind_type.get(name)

                if type_:
                    if not isinstance(obj,type_):
                        raise TypeError("%s must be %s" % (name,type_))

            return func(*args,**kwargs)

        return wrap
    return decorator

@type_assert(int,list,str)
def f(a,b,c):
    pass

f(5,[],'abc')


@type_assert(c = str)
def f(a,b,c):
    pass

f(5,[],111)




