'''
str  int
'''
# str
# # s = ''
# # print(s.isspace())
# int
'''
list:
'''
lis = [11,22,33,44,55]
# for i in range(len(lis)):
#     print(i)       # i = 0              i = 1               i = 2
#     del lis[i]
#     print(lis)  #  [11,22,33,44,55]   [22, 44, 55]          [22, 44]

#第一种
# lis = lis[::2]
# print(lis)

#第二种
# l1 = []
# for i in lis:
#     if lis.index(i) % 2 == 0:
#         l1.append(i)
# lis = l1
# print(lis)

# lis = [11,22,33,44,55]
# # for i in range(len(lis)-1,-1,-1):
# #     if i % 2 == 1:
# #         print(i)
# #         del lis[i]
# #         print(lis)
# # print(lis)

# dic = dict.fromkeys([1,2,3],'春哥')
# print(dic)
# dic = dict.fromkeys([1,2,3],[])
# print(dic)  # {1: [], 2: [], 3: []}
# dic[1].append('袁姐')
# print(dic)
# dic[2].extend('二哥')
# print(dic)


# l1 = []
# l2 = l1
# l3 = l1
# l3.append('a')
# print(l1,l2,l3)

# dic = {'k1':'v1','k2':'v2','a3':'v3'}
# dic1 = {}
#
# for i in dic:
#     if 'k' not in i:
#         dic1.setdefault(i,dic[i])
# dic = dic1
# print(dic)
# l = []
# for i in dic:
#     if 'k' in i:
#         l.append(i)
# for i in l:
#     del dic[i]
# print(dic)

# 转化成bool值
# 0 ''  [] () {} set()

#元祖  如果元祖里面只有一个元素且不加,那此元素是什么类型，就是什么类型。
# tu1 = (1)
# tu2 = (1,)
# print(tu1,type(tu1))
# print(tu2,type(tu2))
# tu1 = ([1])
# tu2 = ([1],)
# print(tu1,type(tu1))
# print(tu2,type(tu2))
# dic = dict.fromkeys([1,2,3,],3)
# dic[1] = 4
# print(dic)


