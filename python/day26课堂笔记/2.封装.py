# class Room:
#     def __init__(self,name,length,width):
#         self.__name = name
#         self.__length = length
#         self.__width = width
#     def get_name(self):
#         return self.__name
#     def set_name(self,newName):
#         if type(newName) is str and newName.isdigit() == False:
#             self.__name = newName
#         else:
#             print('不合法的姓名')
#     def area(self):
#         return self.__length * self.__width
#
# jin = Room('金老板',2,1)
# print(jin.area())
# jin.set_name('2')
# print(jin.get_name())

# 假设父类的私有属性 能被 子类调用么
# class Foo:
#     __key = '123'       # _Foo__key
#
# class Son(Foo):
#     print(Foo.__key)     # _Son__key


# 会用到私有的这个概念de场景
#1.隐藏起一个属性 不想让类的外部调用
#2.我想保护这个属性，不想让属性随意被改变
#3.我想保护这个属性，不被子类继承



