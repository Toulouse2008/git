# 练习一：在终端输出如下信息
#
# 小明，10岁，男，上山去砍柴
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山去砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健
# 老张…
def shangshan():
    print('%s,%s岁,%s,上山去砍柴')

def drive():
    print('%s,%s岁,%s,开车去东北')

def favor():
    print('%s,%s岁,%s,最爱大保健')

# shangshan('小明','10','男')
# drive('小明','10','男')

# 非常明显的处理一类事物，这些事物都具有相似的属性和功能
# 当有几个函数 需要反反复复传入相同的参数的时候，就可以考虑面向对象
# 这些参数都是对象的属性
# class Person:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def shangshan(self):
#         print('%s,%s岁,%s,上山去砍柴'%(self.name,self.age,self.sex))
#     def drive(self):
#         print('%s,%s岁,%s,开车去东北'%(self.name,self.age,self.sex))
#     def favor(self):
#         print('%s,%s岁,%s,最爱大保健'%(self.name,self.age,self.sex))
#
# ming = Person('小明','10','男')
# ming.shangshan()
# ming.drive()
# ming.favor()
# zhang = Person('老张','90','男')
# zhang.shangshan()
# zhang.drive()
# zhang.favor()

# circle 属性 半径 ，两个方法：求周长和面积
# 2pir pir**2
# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return pi*(self.r**2)
#     def perimeter(self):
#         return 2*pi*self.r
#
# c1 = Circle(6)
# print(c1.area())
# print(c1.perimeter())

# 定义类
# init方法
# self是什么 self拥有属性都属于对象
# 类中可以定义静态属性
# 类中可以定义方法，方法都有一个必须传的参数self
# 实例化
# 实例、对象
# 对象查看属性
# 对象调用方法

# 正方形 周长和面积
# 完成上午的作业 人狗大战
# 默写 4.交互文件


