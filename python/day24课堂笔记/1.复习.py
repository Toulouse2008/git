# 面向对象编程
# 思想 ：角色的抽象,创建类，创建角色（实例化），操作这些实例
# 面向对象的关键字
# class 类名:
#     静态属性 = 'aaa'
#     def __init__(self):pass
#
# 类名.静态属性  #—— 存储在类的命名空间里
# 对象 = 类名()  # 实例化：创造了一个self对象，执行init方法，返回self对象给外部
# 对象.属性
# 对象.方法    # 类名.方法(对象)
# 对象可以使用静态变量？ True
# 类可以使用对象里的属性么？ False

# 组合
# 一个类的对象是另外一个类对象的属性
# 什么有什么的关系

# class A:
#     def __init__(self):
#         self.name = 'egon'
#
# class B:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
# b = B(18,1,17)
# a = A()
# a.birth = b
# b.year
# a.birthclass A:
#     def __init__(self):
#         self.name = 'egon'
#
# class B:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
# b = B(18,1,17)
# a = A()
# a.birth = b
# b.year
# a.birth






