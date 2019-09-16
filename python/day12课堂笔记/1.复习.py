# 复习
# 讲作业
# 装饰器的进阶
    # functools.wraps
    # 带参数的装饰器
    # 多个装饰器装饰同一个函数
# 周末的作业
    # 文件操作
    # 字符串处理
    # 输入输出
    # 流程控制

# 装饰器
# 开发原则 ： 开放封闭原则
# 装饰器的作用 ：在不改变原函数的调用方式的情况下，在函数的前后添加功能
# 装饰器的本质 ： 闭包函数

# def wrapper(func):
#     def inner(*args,**kwargs):
#         print('在被装饰的函数执行之前做的事')
#         ret = func(*args,**kwargs)
#         print('在被装饰的函数执行之后做的事')
#         return ret
#     return inner
#
# @wrapper   #holiday = wrapper(holiday)
# def holiday(day):
#     print('全体放假%s天'%day)
#     return '好开心'
#
# ret = holiday(3)
# print(ret)


# def outer(*args):
#     print(args)
#     print(*args)
#     def inner(*args):
#         print('inner : ',args)
#     inner(*args)
#
#
# outer(1,2,3,4)   #==outer(*[1,2,3,4])  #==outer(*(1,2,3,4))




