#绝对路径
# f = open('d:\模特主妇护士班主任.txt',mode='r',encoding='UTF-8')
# content = f.read()
# print(content)
# f.close()

#bytes ---->str
# f = open('模特主妇护士班主任',mode='r',encoding='utf-8')
# content = f.read()
# f.write('fjsdlk')
# f.close()

# f = open('模特主妇护士班主任',mode='rb',)
# content = f.read()
# print(content)
# f.close()
# f = open('log',mode='r+',encoding='utf-8')
# print(f.read())
# f.close()

# f = open('log',mode='r+b')
# print(f.read())
# f.write('大猛，小孟'.encode('utf-8'))
# f.close()



#对于w:没有此文件就会创建文件
# f = open('log',mode='w',encoding='utf-8')
# f.write('骑兵步兵')
# f.close()

# 先将源文件的内容全部清除，在写。
# f = open('log',mode='w',encoding='utf-8')
# f.write('附近看到类似纠纷')
# f.close()


# f = open('log',mode='w+',encoding='utf-8')
# f.write('aaa')
# f.seek(0)
# print(f.read())
# f.close()


# f = open('log',mode='wb')
# f.write('附近看到类似纠纷'.encode('utf-8'))
# f.close()

# f = open('log',mode='a',encoding='utf-8')
# f.write('佳琪')
# f.close()
#
# f = open('log',mode='a',encoding='utf-8')
# f.write('佳琪')
# f.close()



# f = open('log',mode='a+',encoding='utf-8')
# f.write('佳琪')
# f.seek(0)
# print(f.read())
# f.close()


# f = open('log',mode='ab')
# f.write('佳琪'.encode('utf-8'))
# f.close()


#功能详解

# obj = open('log',mode='r+',encoding='utf-8')
# content = f.read(3)  # 读出来的都是字符
# f.seek(3)  # 是按照字节定光标的位置
# f.tell() 告诉你光标的位置
# print(f.tell())
# content = f.read()
# print(content)
# f.tell()
# f.readable()  # 是否刻度
# line = f.readline()  # 一行一行的读
# line = f.readlines()  # 每一行当成列表中的一个元素，添加到list中
# f.truncate(4)
# for line in f:
#     print(line)
# f.close()







# f = open('log',mode='a+',encoding='utf-8')
# f.write('佳琪')
# count = f.tell()
# f.seek(count-9)
# print(f.read(2))
# f.close()

# with open('log',mode='r+',encoding='utf-8') as f,\
#         open('log',mode='w+',encoding='utf-8') as f1:

