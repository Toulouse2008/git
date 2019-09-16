#bool  True False

#int ----> str
i = 1
s = str(i)
#str ---> int
s = '123'
i = int(s)

#int ----->bool  只要是0 ----》False  非0就是True
i = 3
b = bool(i)
print(b)
#bool----> int
#True   1
#False  0
'''
ps:
while True:
    pass
while 1: 效率高
    pass
'''

#str --->bool

#s = "" -----> False
#非空字符串都是True
#s = "0" -----> True

# s
# if s:
#     print('你输入的为空，请重新输入')
# else:
#     pass
