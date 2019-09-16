#列表、元祖
#字典
#集合、frozenset
#字符串
#堆栈 : 先进后出
#队列 ：先进先出 FIFO

# from collections import namedtuple
# Point = namedtuple('point',['x','y','z'])
# p1 = Point(1,2,3)
# p2 = Point(3,2,1)
# print(p1.x)
# print(p1.y)
# print(p1,p2)

#花色和数字
# Card = namedtuple('card',['suits','number'])
# c1 = Card('红桃',2)
# print(c1)
# print(c1.number)
# print(c1.suits)

#队列
# import queue
# q = queue.Queue()
# q.put([1,2,3])
# q.put(5)
# q.put(6)
# print(q)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())   # 阻塞
# print(q.qsize())

# from collections import deque
# dq = deque([1,2])
# dq.append('a')   # 从后面放数据  [1,2,'a']
# dq.appendleft('b') # 从前面放数据 ['b',1,2,'a']
# dq.insert(2,3)    #['b',1,3,2,'a']
# print(dq.pop())      # 从后面取数据
# print(dq.pop())      # 从后面取数据
# print(dq.popleft())  # 从前面取数据
# print(dq)

#有序字典
# from collections import  OrderedDict
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od) # OrderedDict的Key是有序的
# print(od['a'])
# for k in od:
#     print(k)

# from collections import defaultdict
# d = defaultdict(lambda : 5)
# print(d['k'])

