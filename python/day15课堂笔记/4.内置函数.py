# print()
# input()
# len()
# type()
# open()
# tuple()
# list()
# int()
# bool()
# set()
# dir()
# id()
# str()


# print(locals())  #返回本地作用域中的所有名字
# print(globals()) #返回全局作用域中的所有名字
# global 变量
# nonlocal 变量

#迭代器.__next__()
# next(迭代器)
# 迭代器 = iter(可迭代的)
# 迭代器 = 可迭代的.__iter__()

# range(10)
# range(1,11)
# print('__next__' in dir(range(1,11,2)))

# dir 查看一个变量拥有的方法
# print(dir([]))
# print(dir(1))

# help
# help(str)

# 变量
# print(callable(print))
# a = 1
# print(callable(a))
# print(callable(globals))
# def func():pass
# print(callable(func))

import time
# t = __import__('time')
# print(t.time())

# 某个方法属于某个数据类型的变量，就用.调用
# 如果某个方法不依赖于任何数据类型，就直接调用  —— 内置函数 和 自定义函数

# f = open('1.复习.py')
# print(f.writable())
# print(f.readable())

#id
#hash - 对于相同可hash数据的hash值在一次程序的执行过程中总是不变的
#     - 字典的寻址方式
# print(hash(12345))
# print(hash('hsgda不想你走，nklgkds'))
# print(hash(('1','aaa')))
# print(hash([]))

# ret = input('提示 ： ')
# print(ret)

# print('我们的祖国是花园',end='')  #指定输出的结束符
# print('我们的祖国是花园',end='')
# print(1,2,3,4,5,sep='|') #指定输出多个值之间的分隔符
# f = open('file','w')
# print('aaaa',file=f)
# f.close()

# import time
# for i in range(0,101,2):
#      time.sleep(0.1)
#      char_num = i//2
#      per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
#          if i == 100 else '\r%s%% : %s' % (i,'*'*char_num)
#      print(per_str,end='', flush=True)
#progress Bar

# exec('print(123)')
# eval('print(123)')
# print(eval('1+2+3+4'))   # 有返回值
# print(exec('1+2+3+4'))   #没有返回值
# exec和eval都可以执行 字符串类型的代码
# eval有返回值  —— 有结果的简单计算
# exec没有返回值   —— 简单流程控制
# eval只能用在你明确知道你要执行的代码是什么

# code = '''for i in range(10):
#     print(i*'*')
# '''
# exec(code)

# code1 = 'for i in range(0,10): print (i)'
# compile1 = compile(code1,'','exec')
# exec(compile1)

# code2 = '1 + 2 + 3 + 4'
# compile2 = compile(code2,'','eval')
# print(eval(compile2))

# code3 = 'name = input("please input your name:")'
# compile3 = compile(code3,'','single')
# exec(compile3) #执行时显示交互命令，提示输入
# print(name)
# name #执行后name变量有值
# "'pythoner'"


# 复数 —— complex
# 实数 ： 有理数
#         无理数
# 虚数 ：虚无缥缈的数
# 5 + 12j  === 复合的数 === 复数
# 6 + 15j

# 浮点数（有限循环小数，无限循环小数）  != 小数 ：有限循环小数，无限循环小数，无限不循环小数
# 浮点数
    #354.123 = 3.54123*10**2 = 35.4123 * 10
# f = 1.781326913750135970
# print(f)

# print(bin(10))
# print(oct(10))
# print(hex(10))

# print(abs(-5))
# print(abs(5))

# print(divmod(7,2))   # div出发 mod取余
# print(divmod(9,5))   # 除余

# print(round(3.14159,3))
# print(pow(2,3))   #pow幂运算  == 2**3
# print(pow(3,2))
# print(pow(2,3,3)) #幂运算之后再取余
# print(pow(3,2,1))

# ret = sum([1,2,3,4,5,6])
# print(ret)

# ret = sum([1,2,3,4,5,6,10],)
# print(ret)

# print(min([1,2,3,4]))
# print(min(1,2,3,4))
# print(min(1,2,3,-4))
# print(min(1,2,3,-4,key = abs))

print(max([1,2,3,4]))
print(max(1,2,3,4))
print(max(1,2,3,-4))
print(max(1,2,3,-4,key = abs))

