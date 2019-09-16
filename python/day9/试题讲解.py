# li = ['alex','wusir','rain']
# s1 = '*'.join(li)
# print(s1)
#1-2+3-4+5.......+99
sum = 0
for i in range(1,100):
    if i % 2 == 0:
        sum = sum - i
    else:
        sum += i

#12，使用range打印100,99,98，....1,0(2分)

# for i in range(100,-1,-1):
#     print(i)

# count = 0
# content = input('>>>')
# for i in range(len(content)):
#     if i % 2 == 1 and content[i].isdigit():
#         count += 1
# print(count)
'''
16，实现一个整数加法计算器：（6分）            
如：content = input(‘请输入内容:’)  # 如用户输入：5+8+7....(最少输入两个数相加)，然后进行分割再进行计算，将最后的计算结果添加到此字典中(替换None)：
dic={‘最终计算结果’:None}。

'''
# content = input('请输入内容:')  # 5+8+7。。。
# content_list = content.split('+')
# print(content_list)
# sum = 0
# for i in content_list:
#     sum = sum + int(i)
# print(sum)

# i = '7       '
# print(int(i.strip()))

# li = [11,22,33,44,55,77,88,99,90]
# result = {'key1':[],'key2':[]}
# for row in li:
# li = [11,22,33,44,55,77,88,99,90]
# result = {}
# for row in li:
#     if row > 66:
#         if 'key1' not in result:
#             result['key1']=[]
#         result['key1'].append(row)
#     else:
#         if 'key2' not in result:
#             result['key2']=[]  # result = {'key2':[]}
#         result['key2'].append(row)
# print(result)

# li = [11,22,33,44,55,77,88,99,90]
# result = {}
# for row in li:
#     result.setdefault('key1',[])
#     result.setdefault('key2',[])
#     if row > 66:
#         result['key1'].append(row)
#     else:
#         result['key2'].append(row)
user_list = [
    {'username':'barry','password':'1234'},
    {'username':'alex','password':'asdf'},
             ]
board = ['张三','李小四','王二麻子']
while 1:
    username = input('用户名：')
    if username.upper() == 'Q':break
    password = input('密码：')
    for i in board:
        if i in username:
            username = username.replace(i,'*'*len(i))
    user_list.append({'username':username,'password':password})
    print({'username':username,'password':password})
    print(user_list)