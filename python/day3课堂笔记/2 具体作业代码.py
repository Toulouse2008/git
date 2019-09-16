# print(5 < 4 or 3)
# print(2 > 1 or 6)
# print(3 > 1 and 0)
# #计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和
# 1-2+3.。。，。+99
# i=1
# sum=0
# while i <100:
#     if i==88:
#         i += 1
#         continue
#     if i%2!=0:
#         sum=sum+i
#     else:
#         sum=sum-i
#     i += 1
# print(sum)

# #计算 1 - 2 + 3 ... -99 中除了88意外所有数的总和
i=0
j=-1
sum=0
while i<99:
    i=i+1
    if i==88:
        continue
    else:
        j = -j
        sum=sum+i*j

print(sum)
#
# sum=sum+i
#
# i       j       sum
# 1       1       0 + 1*1
# 2       -1      0 + 1*1 +2*-1
# 3        1
# 87       1      。。。。。 + 87*1
# 89        -1
# i = input('数字')
# if i=='2':
#     print(1212)
# if i == '2':
#     print(11111)
# else:print(666)

#⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
# i = 3
# username = "yangxiaoer"
# password = "123456"
# while i>=0:
#     name = input("请输入你的用户名：")
#     if name == username:
#         passwd = input("请输入你的密码：")
#         if passwd == password:
#             print("登录成功。请稍后")
#             print('''
#             username: %s
#             password: %s
#             '''%(username,password))
#             break
#         else:
#             print("你的密码错误 请重新输入")
#             print("你还有%s次机会" % (i-1))
#             if i == 0:
#                 print('您的机会已经用完，结束本次操作')
#                 break
#             continue
#     else:
#         print("你的用户名错误！请重新输入")
#         print("你还有%s次机会"%(i-1))
#     i -= 1
username = "yangxiaoer"
password = "123456"
i = 3
while i > 0:
    zh = input("请输入你的账号:")
    i -= 1
    if zh == username:
        mm = input("请输入你的密码:")
        if mm == password:
            print("验证成功.正在登陆......")
            print('''恭喜你登陆成功!
            欢迎用户进入
            用户名 :%s
            密码   :%s
            '''%(zh,mm))
            break
        else:
            if i == 0:
                print("你的机会已经没了!game over 下次见!")
                answer = input('再试试？Y or N')
                if answer == 'Y':
                    i = 3
            print("密码错误,请重新输入")
            print("你还有"+str(i)+"次机会")
    else:
        print("请输入正确的用户名!")
        if i == 0:
            print("你的机会已经没了!")
            answer = input('再试试？Y or N')
            if answer == 'Y':
                i = 3
        print("你还有" + str(i) + "次机会")
else:
    print('你TM要不要脸')