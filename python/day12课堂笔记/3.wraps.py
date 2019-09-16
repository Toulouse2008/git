from functools import wraps
def wrapper(func):  #func = holiday
    @wraps(func)
    def inner(*args,**kwargs):
        print('在被装饰的函数执行之前做的事')
        ret = func(*args,**kwargs)
        print('在被装饰的函数执行之后做的事')
        return ret
    return inner

@wrapper   #holiday = wrapper(holiday)
def holiday(day):
    '''这是一个放假通知'''
    print('全体放假%s天'%day)
    return '好开心'

print(holiday.__name__)
print(holiday.__doc__)
ret = holiday(3)   #inner
print(ret)


# def wahaha():
#     '''
#     一个打印娃哈哈的函数
#     :return:
#     '''
#     print('娃哈哈')

# print(wahaha.__name__) #查看字符串格式的函数名
# print(wahaha.__doc__)  #document
