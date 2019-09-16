# 装饰器形成的过程 : 最简单的装饰器 有返回值的 有一个参数 万能参数
# 装饰器的作用
# 原则 ：开放封闭原则
# 语法糖 ：@
# 装饰器的固定模式

#不懂技术


import time
# print(time.time()) # 获取当前时间
# time.sleep(10)  #让程序在执行到这个位置的时候停一会儿


# def timmer(f):    #装饰器函数
#     def inner():
#         start = time.time()
#         ret = f()       #被装饰的函数
#         end = time.time()
#         print(end - start)
#         return ret
#     return inner
#
# @timmer         #语法糖 @装饰器函数名
# def func():     #被装饰的函数
#     time.sleep(0.01)
#     print('老板好同事好大家好')
#     return '新年好'
# # func = timmer(func)
# ret = func()   #inner()
# print(ret)
# 装饰器的作用 —— 不想修改函数的调用方式 但是还想在原来的函数前后添加功能
# timmer就是一个装饰器函数，只是对一个函数 有一些装饰作用

# 原则： 开放封闭原则
#   开放 ： 对扩展是开放的
#   封闭 ： 对修改是封闭的

# 封版

# def outer():
#     def inner():
#         return 'inner'
#     inner()
#
# outer()

#装饰带参数函数的装饰器
# def timmer(f):    #装饰器函数
#     def inner(*args,**kwargs):
#         #(1,2) /(1)
#         start = time.time()
#         ret = f(*args,**kwargs)  #f(1,2)       #被装饰的函数
#         end = time.time()
#         print(end - start)
#         return ret
#     return inner
#
# @timmer         #语法糖 @装饰器函数名
# def func(a,b):     #被装饰的函数
#     time.sleep(0.01)
#     print('老板好同事好大家好',a,b)
#     return '新年好'
#
# @timmer         #语法糖 @装饰器函数名
# def func1(a):     #被装饰的函数
#     time.sleep(0.01)
#     print('老板好同事好大家好',a)
#     return '新年好'
# # func = timmer(func)
# ret = func(1,2)   #inner()
# ret = func(1,b = 2)   #inner()
# print(ret)

# def wrapper(f):    #装饰器函数，f是被装饰的函数
#     def inner(*args,**kwargs):
#         '''在被装饰函数之前要做的事'''
#         ret = f(*args,**kwargs)    #被装饰的函数
#         '''在被装饰函数之后要做的事'''
#         return ret
#     return inner
#
# @wrapper         #语法糖 @装饰器函数名
# def func(a,b):     #被装饰的函数
#     time.sleep(0.01)
#     print('老板好同事好大家好',a,b)
#     return '新年好'

# def wrapper():
#     def inner():
#         pass
#     return inner

def wrapper(func):   #qqxing
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)   #被装饰的函数
        return ret
    return inner

@wrapper        #qqxing = wrapper(qqxing)
def qqxing():
    print(123)

ret = qqxing()   #inner

#
# 讲解元旦作业 扩展装饰器

