#len
# s = '金老板小护士'
# len(s)
# def my_len():  #自定义函数
#     i = 0
#     for k in s:
#         i += 1
#     print(i)
#
# length = my_len()
# print(length)
# 函数
# 定义了之后，可以在任何需要它的地方调用
# 没有返回长度，只是单纯的打印

#返回的重要性
#a,b
#len(a)  #内置函数
#len(b)

# def my_len():  #自定义函数
#     i = 0
#     for k in s:
#         i += 1
#     return i  #返回值
#
# length = my_len()
# print(length)

#len()
#1.不能变，只能计算s字符串的长度
#2.只是输出了结果

#返回值
#返回值的3种情况
    # 没有返回值 —— 返回None
        # 不写return
        # 只写return:结束一个函数的继续
        # return None  —— 不常用
    # 返回1个值
        # 可以返回任何数据类型
        # 只要返回就可以接收到
        # 如果在一个程序中有多个return，那么只执行第一个
    # 返回多个值
        # 用多个变量接收：有多少返回值就用多少变量接收
        # 用一个变量接收: 得到的是一个元组

# def func():
#     l = ['金老板','二哥']
#     for i in l:
#         print(i)
#         if i=='金老板':
#             return None
#     print('='*10)
# ret = func()
# print(ret)

# def func():
#     return {'k':'v'}
# print(func())

# def func2():
#     return 1,2,3  #return 1,2,3
#
# r= func2()
# print(r)


# def my_len(s):  #自定义函数只需要0个参数，接收参数,形式参数，形参
#     i = 0
#     for k in s:
#         i += 1
#     return i  #返回值
#
# ret = my_len('金老板小护士')  #传递参数：传参，实际参数，实参
# ret = my_len([1,2,3,4,5])  #传递参数：传参
# print(ret)

#什么叫参数？
#参数的语法
#形参和实参的概念


# def f2(l1):
#     f1(l1)
#     for i in l1:
#         print(i)
#
# def f1(l1):
#     for i in l1:
#         print(i)
#
# f2([1,2,3,4])

#参数
    #没有参数
        #定义函数和调用函数时括号里都不写内容
    #有一个参数
        #传什么就是什么
    #有多个参数
        #位置参数
# def my_sum(a,b):
#     print(a,b)
#     res = a+b  #result
#     return res
#
# ret = my_sum(1,2)
# print(ret)

#站在实参的角度上：
    #按照位置传参
    #按照关键字传参
    #混着用可以:但是 必须先按照位置传参，再按照关键字传参数
            #  不能给同一个变量传多个值

#站在形参的角度上
    #位置参数：必须传,且有几个参数就传几个值
    #默认参数: 可以不传，如果不传就是用默认的参数，如果传了就用传的
# def classmate(name,sex='男'):
#     print('%s : %s'%(name,sex))
#
# classmate('二哥')
# classmate('小孟')
# classmate('大猛')
# classmate('朗哥','女')

#只有调用函数的时候
    #按照位置传 ： 直接写参数的值
    #按照关键字： 关键字 = 值

#定义函数的时候：
    #位置参数 ： 直接定义参数
    #默认参数，关键字参数 ：参数名 = '默认的值'
    #动态参数 : 可以接受任意多个参数
                #参数名之前加*，习惯参数名args，
                #参数名之前加**，习惯参数名kwargs
    #顺序：位置参数，*args,默认参数,**kwargs

# def classmate(name,sex):
#     print('%s : %s'%(name,sex))
#
# classmate('二哥','男')
# classmate(sex='男',name = '二哥')

# def classmate(name,sex='男'):
#     print('%s : %s'%(name,sex))
#
# classmate('二哥')
# classmate('朗哥',sex= '女')

# def sum(*args):
#     n = 0
#     for i in args:
#         n+=i
#     return n
#
# print(sum(1,2))
# print(sum(1,2,3))
# print(sum(1,2,3,4))

# def func(**kwargs):
#     print(kwargs)
#
# func(a = 1,b = 2,c =3)
# func(a = 1,b = 2)
# func(a = 1)

# 动态参数有两种：可以接受任意个参数
    #*args   ： 接收的是按照位置传参的值，组织成一个元组
    #**kwargs： 接受的是按照关键字传参的值，组织成一个字典
    #args必须在kwargs之前
# def func(*args,default = 1,**kwargs):
#     print(args,kwargs)
#
# func(1,2,3,4,5,default=2,a = 'aaaa',b = 'bbbb',)

#动态参数的另一种传参方式
# def func(*args):#站在形参的角度上，给变量加上*，就是组合所有传来的值。
#     print(args)
#
# func(1,2,3,4,5)
# l = [1,2,3,4,5]
# func(*l)  #站在实参的角度上，给一个序列加上*，就是将这个序列按照顺序打散

# def func(**kwargs):
#     print(kwargs)
#
# func(a=1,b=2)
# d = {'a':1,'b':2} #定义一个字典d
# func(**d)

#函数的注释
# def func():
#     '''
#     这个函数实现了什么功能
#     参数1：
#     参数2：
#     :return: 是字符串或者列表的长度
#     '''
#     pass

    # 默认参数的陷阱
# 文件的修改
# 函数
#1.函数的定义 def
#2.函数的调用
#3.函数的返回值 return
#4.函数的参数
    #形参：
        # 位置参数 ： 必须传
        # *args ：可以接收任意多个位置参数
        # 默认参数 ： 可以不传
        # **kwargs ： 可以接收多个关键字参数
    #实参：按照位置传参，按照关键字传参

#函数
    #内置函数
    #自定义函数 ！！！！！