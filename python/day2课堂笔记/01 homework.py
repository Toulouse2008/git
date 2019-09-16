#1、使用while循环输入 1 2 3 4 5 6 8 9 10
'''
count = 0
while count < 10:
    count += 1  # count = count + 1
    if count == 7:
        print(' ')
    else:
        print(count)

count = 0
while count < 10:
    count += 1  # count = count + 1
    if count == 7:
        continue
    print(count)
'''
#3、输出 1-100 内的所有奇数
#方法一：
# count = 1
# while count < 101:
#     print(count)
#     count += 2
#方法二：
# count = 1
# while count < 101:
#     if count % 2 == 1:
#         print(count)
#     count += 1

#5、求1-2+3-4+5 ... 99的所有数的和
# sum = 0
# count = 1
# while count < 100:
#     if count % 2 == 0:
#         sum = sum - count
#     else:
#         sum = sum + count
#     count += 1
# print(sum)

#6、用户登陆（三次机会重试）
#input 心中有账号，密码 while

i = 0
while i < 3:
    username = input('请输入账号：')
    password = int(input('请输入密码：'))
    if username == '咸鱼哥' and password == 123:
        print('登录成功')
    else:
        print('登录失败请重新登录')
    i += 1