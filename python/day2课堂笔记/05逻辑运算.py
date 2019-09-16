#and or not
#优先级，（）> not > and > or
# print(2 > 1 and 1 < 4)
# print(2 > 1 and 1 < 4 or 2 < 3 and 9 > 6 or 2 < 4 and 3 < 2)
# T or T or F
#T or F
# print(3>4 or 4<3 and 1==1)  # F
# print(1 < 2 and 3 < 4 or 1>2)  # T
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)  # T
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)  # F
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # F
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # F

#ps  int  ----> bool   非零转换成bool True   0 转换成bool 是False
# print(bool(2))
# print(bool(-2))
# print(bool(0))
# #bool --->int
# print(int(True))   # 1
# print(int(False))  # 0


'''x or y x True，则返回x'''
# print(1 or 2)  # 1
# print(3 or 2)  # 3
# print(0 or 2)  # 2
# print(0 or 100)  # 100


# print(2 or 100 or 3 or 4)  # 2

# print(0 or 4 and 3 or 2)
'''x and y x True，则返回y'''
# print(1 and 2)
# print(0 and 2)
print(2 or 1 < 3)
print(3 > 1 or 2 and 2)


