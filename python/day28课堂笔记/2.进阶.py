dic = {'k':'v'}
# 对象 ： 存储属性 和调用方法
dic['k'] = 'v'
# class Foo:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __getitem__(self, item):
#         if hasattr(self,item):
#             return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
# f = Foo('egon',38,'男')
# print(f['name'])
# f['hobby'] = '男'
# print(f.hobby,f['hobby'])
# del f.hobby      # object 原生支持  __delattr__
# del f['hobby']   # 通过自己实现的
# print(f.__dict__)

# __init__ 初始化方法
# __new__  构造方法 : 创建一个对象
class A:
    def __init__(self):
        self.x = 1
        print('in init function')
    # def __new__(cls, *args, **kwargs):
    #     print('in new function')
    #     return object.__new__(A, *args, **kwargs)

# a1 = A()
# a2 = A()
# a3 = A()
# print(a1)
# print(a2)
# print(a3)
# print(a.x)

# 设计模式
# 23种
# 单例模式
# 一个类 始终 只有 一个 实例
# 当你第一次实例化这个类的时候 就创建一个实例化的对象
# 当你之后再来实例化的时候 就用之前创建的对象

# class A:
#     __instance = False
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance:
#             return cls.__instance
#         cls.__instance = object.__new__(cls)
#         return cls.__instance
#
# egon = A('egg',38)
# egon.cloth = '小花袄'
# nezha = A('nazha',25)
# print(nezha)
# print(egon)
# print(nezha.name)
# print(egon.name)
# print(nezha.cloth)


# class A:
#     def __init__(self,name):
#         self.name = name
#
#     def __eq__(self, other):
#         if self.__dict__ == other.__dict__:
#             return True
#         else:
#             return False
#
# ob1 = A('egon')
# ob2 = A('egg')
# print(ob1 == ob2)

# hash()   #__hash__
# class A:
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#     def __hash__(self):
#         return hash(self.name+self.sex)
#
# a = A('egon','男')
# b = A('egon','nv')
# print(hash(a))
# print(hash(b))
import json
from collections import namedtuple
Card = namedtuple('Card',['rank','suit'])   # rank 牌面的大小 suit牌面的花色
# class FranchDeck:
#     ranks = [str(n) for n in range(2,11)] + list('JQKA')   # 2-A
#     suits = ['红心','方板','梅花','黑桃']
#
#     def __init__(self):
#         self._cards = [Card(rank,suit) for rank in FranchDeck.ranks
#                                         for suit in FranchDeck.suits]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, item):
#         return self._cards[item]
#
#     def __setitem__(self, key, value):
#         self._cards[key] = value
#
#     def __str__(self):
#         return json.dumps(self._cards,ensure_ascii=False)

# deck = FranchDeck()
# print(deck[10])
# from random import choice
# print(choice(deck))
# # print(choice(deck))
# from random import shuffle
# shuffle(deck)
# print(deck[10])
# print(deck)
# print(deck[:5])

# 内置函数 内置的模块 内置的基础类型 < --- >类的内置方法
# ==    __eq__
# len() __len__

# 100 名字 和 性别 年龄不同
# set
# class A:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     # def __eq__(self, other):
#     #     if self.name == other.name and self.sex == other.sex:
#     #         return True
#     #     return False
#
#     def __hash__(self):
#         return hash(self.name + self.sex)
# a = A('egg','男',38)
# b = A('egg','男',37)
# print(set((a,b)))   # unhashable

# set 依赖对象的 hash eq












