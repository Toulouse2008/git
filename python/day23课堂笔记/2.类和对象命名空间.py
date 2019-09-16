# 类里 可以定义两种属性
# 静态属性
# 动态属性
class Course:
    language = ['Chinese']
    def __init__(self,teacher,course_name,period,price):
        self.teacher = teacher
        self.name = course_name
        self.period = period
        self.price = price
    def func(self):
        pass

# Course.language = 'English'
# Course.__dict__['language'] = 'Chinese'
# print(Course.language)
python = Course('egon','python','6 months',20000)
linux = Course('oldboy','linux','6 months',20000)
#['chinese']
python.language = ''
# print(python.language)
# print(linux.language)
# Course.language = 'Chinese'
# print(python.language)
# print(linux.language)

# del python.language
# print(python.language)
# print(python.__dict__)
# print(Course.language)
# print(linux.language)
# print(linux.__dict__)
# 类中的静态变量 可以被对象和类调用
# 对于不可变数据类型来说，类变量最好用类名操作
# 对于可变数据类型来说，对象名的修改是共享的，重新赋值是独立的

# 模拟人生
# class Person:
#     money = 0
#     def work(self):
#         Person.money += 1000
#
# mother = Person()
# father = Person()
# Person.money += 1000
# Person.money += 1000
# print(Person.money)
# mother.work()
# father.work()


# 创建一个类，每实例化一个对象就计数
# 最终所有的对象共享这个数据
# class Foo:
#     count = 0
#     def __init__(self):
#         Foo.count += 1
#
# f1 = Foo()
# f2 = Foo()
# print(f1.count)
# print(f2.count)
# f3 = Foo()
# print(f1.count)


# 认识绑定方法
# def func():pass
# print(func)
#
# class Foo:
#     def func(self):
#         print('func')
#     def fun1(self):
#         pass
# f1 = Foo()
# print(Foo.func)
# print(f1.func)
# print(f1.fun1)
#<bound method Foo.func of f1>

# 包 —— __init__
# import package —— 类的实例化的过程
# import time
# time.time()


# 类里的名字有 类变量（静态属性量）+ 方法名（动态属性）
# 对象里的名字 对象属性
# 对象 —— > 类
# 对象找名字 ： 先找自己的 找类的 再找不到就报错
# 对象修改静态属性的值
    # 对于不可变数据类型来说，类变量最好用类名操作
    # 对于可变数据类型来说，对象名的修改是共享的，重新赋值是独立的