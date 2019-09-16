# s = '132a4b5c'
# s1 = s[0]+s[2]+s[1]
# print(s1)
#使用while和for循环分别打印字符串s=’asdfer’中每个元素。
s = 'fkld'
# for i in s:
#     print(i)
# index = 0
# while 1:
#     print(s[index])
#     index += 1
#     if index == len(s):break
#如：content = input(‘请输入内容:’)  # 如用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
# content=input('>>>').strip()
# con1=content.split('+')
#li[]
# num=0
# for i in con1:
#     num+=int(i)
# print(num)
# content=input('>>>').strip()
# index = content.find("+")
# a = int(content[0:index])
# b = int(content[index+1:])
# print(a + b)
#咱们任意输入一串文字+数字 统计出来数字的个数

s = input("请输入：")  # '1234324324fdsaf1fdsaf12'
count = 0
for i in s:
    if i.isdigit():
        count += 1
print(count)