# 登录认证
# 加密 --> 解密
# 摘要算法
# 两个字符串 ：
# import hashlib   # 提供摘要算法的模块
# md5 = hashlib.md5()
# md5.update(b'123456')
# print(md5.hexdigest())
#aee949757a2e698417463d47acac93df


# 不管算法多么不同，摘要的功能始终不变
# 对于相同的字符串使用同一个算法进行摘要，得到的值总是不变的
# 使用不同算法对相同的字符串进行摘要，得到的值应该不同
# 不管使用什么算法，hashlib的方式永远不变

# import hashlib   # 提供摘要算法的模块
# sha = hashlib.md5()
# sha.update(b'alex3714')
# print(sha.hexdigest())

# sha 算法 随着 算法复杂程度的增加 我摘要的时间成本空间成本都会增加

# 摘要算法
# 密码的密文存储
# 文件的一致性验证
    # 在下载的时候 检查我们下载的文件和远程服务器上的文件是否一致
    # 两台机器上的两个文件 你想检查这两个文件是否相等

# 用户注册
# 用户 输入用户名
# 用户输入 密码
# 明文的密码进行摘要 拿到一个密文的密码
# 写入文件

# 用户的登录
# import hashlib
# usr = input('username :')
# pwd = input('password : ')
# with open('userinfo') as f:
#     for line in f:
#         user,passwd,role = line.split('|')
#         md5 = hashlib.md5()
#         md5.update(bytes(pwd,encoding='utf-8'))
#         md5_pwd = md5.hexdigest()
#         if usr == user and md5_pwd == passwd:
#             print('登录成功')


# 1234567890
# abcdefghijk
# 6位
# md5
# 撞库

# 加盐
import hashlib   # 提供摘要算法的模块
# md5 = hashlib.md5(bytes('盐',encoding='utf-8'))
# # md5 = hashlib.md5()
# md5.update(b'123456')
# print(md5.hexdigest())

# 动态加盐
# 用户名 密码
# 使用用户名的一部分或者 直接使用整个用户名作为盐
# import hashlib   # 提供摘要算法的模块
# md5 = hashlib.md5(bytes('盐',encoding='utf-8')+b'')
# # md5 = hashlib.md5()
# md5.update(b'123456')
# print(md5.hexdigest())

#import hashilib
# 做摘要计算的 把字节类型的内容进行摘要处理
# md5 sha
# md5  正常的md5算法 加盐的 动态加盐


# 文件的一致性校验
# 文件的一致性校验这里不需要加盐
# import hashlib
# md5 = hashlib.md5()
# md5.update(b'alex')
# md5.update(b'3714')
# print(md5.hexdigest())

# 作业： 对一个文件进行摘要算法，最后计算出这个文件的md5值。