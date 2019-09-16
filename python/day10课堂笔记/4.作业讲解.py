#2、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func(l):
#     return l[1::2]  #切片
# print(func([1,2,3,4,5]))

# 3、写函数，判断用户传入的值（字符串、列表、元组）长度是否大于5。
# def func(x):
#     return len(x)>5
# if func('abcd'):
#     print('长度确实大于5')

# 4、写函数，检查传入列表的长度，如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(l):
#     return l[:2]
#
# print(func([1,2,3,4]))

# 5、写函数，计算传入字符串中【数字】、【字母】、【空格】 以及 【其他】的个数，并返回结果。
# def func(s):   #'skghfoiw8qpeuqkd'
#     dic = {'num':0,'alpha':0,'space':0,'other':0}
#     for i in s:
#         if i.isdigit():
#             dic['num']+=1
#         elif i.isalpha():
#             dic['alpha'] += 1
#         elif i.isspace():
#             dic['space'] += 1
#         else:
#             dic['other'] += 1
#     return dic
# print(func('+0-0skahe817jashf wet1'))

# 6、写函数，检查用户传入的对象（字符串、列表、元组）
# 的每一个元素是否含有空内容，并返回结果。
# def func(x):
#     if type(x) is str and x:  #参数是字符串
#         for i in x:
#             if i == ' ':
#                 return True
#     elif x and type(x) is list or type(x) is tuple: #参数是列表或者元组
#         for i in x:
#             if not i:
#                 return True
#     elif not x:
#         return True
#
# print(func([]))

#7、写函数，检查传入字典的每一个value的长度,如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
#	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
#	PS:字典中的value只能是字符串或列表
# def func(dic):
#     for k in dic:
#         if len(dic[k]) > 2:
#             dic[k] = dic[k][:2]
#     return dic
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# print(func(dic))

# 8、写函数，接收两个数字参数，返回比较大的那个数字。
# def func(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(func(1,5))

# def func(a,b):
#     return a if a > b else b
# print(func(5,1))

# 三元运算
# a = 1
# b = 5
# c = a if a>b else b   #三元运算
# print(c)

# 变量 = 条件返回True的结果 if 条件 else 条件返回False的结果
#必须要有结果
#必须要有if和else
#只能是简单的情况

# 9、写函数，用户传入修改的文件名，与要修改的内容，
# 执行函数，完成整个文件的批量修改操作（进阶）。
# def func(filename,old,new):
#     with open(filename, encoding='utf-8') as f, open('%s.bak'%filename, 'w', encoding='utf-8') as f2:
#         for line in f:
#             if old in line:  # 班主任:星儿
#                 line = line.replace(old,new)
#             # 写文件
#             f2.write(line)  # 小护士:金老板
#
#     import os
#     os.remove(filename)  # 删除文件
#     os.rename('%s.bak'%filename, filename)  # 重命名文件
