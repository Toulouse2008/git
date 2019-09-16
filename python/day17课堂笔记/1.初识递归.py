#递归函数
    # 了解什么是递归  ： 在函数中调用自身函数
        # 最大递归深度默认是997/998 —— 是python从内存角度出发做得限制
    # 能看懂递归
    # 能知道递归的应用场景
    # 初识递归 ——
    # 算法 —— 二分查找算法
    # 三级菜单 —— 递归实现

# while True:
#     print('从前有座山')

# def story():
#     print('从前有座山')
#     story()
#     print(111)
#
# story()

#RecursionError: maximum recursion depth exceeded while calling a Python object
# 递归的错误，超过了递归的最大深度

# import sys
# sys.setrecursionlimit(1000000)
# n = 0
# def story():
#     global n
#     n += 1
#     print(n)
#     story()
# story()

# 如果递归次数太多，就不适合使用递归来解决问题
# 递归的缺点 ： 占内存
# 递归的优点：  会让代码变简单

# alex 多大       n = 1   age(1) = age(2)+2 = age(n+1) + 2
# alex比egon大两岁
# egon多大？      n = 2   age(2) = age(3) + 2 = age(n+1) +2
# egon比wusir大两岁
# wusir多大       n = 3   age(3) = age(4) + 2 = age(n+1) +2
# wusir比金老板大两岁
# 金老板多大？
# 金老板40了      n = 4   age(4) = 40

# n = 4 age(4) = 40
# n <4  age(n) = age(n+1) +2
def age(n):
    if n == 4:
        return 40
    elif n >0 and n < 4:
        age(n+1) + 2
#
print(age(1))

# # 教你看递归
# def age(1):
#     if 1 == 4:
#         return 40
#     elif 1 > 0 and 1 < 4:
#         return 46
#
# def age(2):
#     if 2 == 4:
#         return 40
#     elif 2 >0 and 2 < 4:
#         age(3) + 2    None +2
#
# def age(3):
#     if 3 == 4:
#         return 40
#     elif 3 >0 and 3 < 4:
#         42
#
# def age(4):
#     if 4 == 4:
#         return 40
#     elif n >0 and n < 4:
#         age(n+1) + 2



