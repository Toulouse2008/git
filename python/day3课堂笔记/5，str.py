#字符串的索引与切片
'''
s = 'ABCDLSESRF'
#索引
# s1 = s[0]
# print(s1)
# s2 = s[2]
# print(s2)
# s3 = s[-1]
# print(s3)
# s4 = s[-2]
# print(s4)
# #ABCD   切片 ：顾头不顾尾
# s5 = s[0:4]
# print(s5)
# s6 = s[0:-1]
# print(s6)
# s7 = s[:]
# s8 = s[0:]
# print(s7,s8)
# s9 = s[0:0]
s = 'ABCDLSESRF'  # s[首:尾:步长]
# s10 = s[0:5:2]
# print(s10)
s11 = s[4:0:-1]
print(s11)
s12 = s[3::-1]
print(s12)
s13 = s[3::-2]
print(s13)
s = 'ABCDLSESRF'
s14 = s[-1::-1]
print(s14)
s15 = s[::-1]
print(s15)
'''

#字符串的操作
s = 'alexWUsir'
s1 = s.capitalize()  # 首字母大写
# print(s1)

# 全大写，全小写
s2 = s.upper()
s21 = s.lower()
# print(s2,s21)
'''
s_str= 'acEQ1'
you_input =input('请输入验证码，不区分大小写')
if s_str.upper() == you_input.upper():
    print('输入成功')
else:
    print('请重新输入')
'''
#大小写翻转
# s3 = s.swapcase()
# print(s3)
# 每个隔开(特殊字符或者数字)的单词首字母大写
# s = 'alex*egon-wusir'
# s4 = s.title()
# print(s4)
# s = 'fade,crazy*w4rri0r_songsong node_3'
# s4 = s.title()
# print(s4)

#居中，空白填充
# s = 'alexWUsir'
# s5 = s.center(20,'~')
# print(s5)

# s = 'alex\tsir'
# s6 = s.expandtabs()
# print(s6)

# s = 'alex二哥'
# #公共方法
# l = len(s)
# print(l)

#以什么开头结尾 endswith
# s = 'alexWUsir'
# s7 =s.startswith('alex')
# s71 = s.startswith('e',2,5)
# print(s71)
'''
if s7:
    pass
elif s.startswith('bl'):
    pass
print(s7)
'''
# find 通过元素找索引，找不到返回-1
#
# index通过元素找索引，找不到报错
# s = 'alexWUsir'
# s8 = s.find('A')
# s81 = s.index('A')
# print(s81,type(s8))

#strip rstrip lstrip
# s = 'alexWUsir%'
# s9 = s.strip('%')
# print(s9)
# s = ' *a%lexWUsi* r%'
# s91 = s.strip(' %*')
# print(s91)

# strip 默认删除前后空格

# username = input('请输入名字：').strip()
# if username =='春哥':
#     print('恭喜春哥发财')

# s = 'alexaa wusirl'
# s10 = s.count('al')
# print(s10)

# split   str ---->list
# s = ';alex;wusir;taibai'
# l = s.split('a')
# print(l)

#format的三种玩法 格式化输出
# s = '我叫{}，今年{}，爱好{}，再说一下我叫{}'.format('太白',36,'girl','太白')
# print(s)
# name = input('请输入名字：')
# s = '我叫{0}，今年{1}，爱好{2}，再说一下我叫{0}'.format(name,36,'girl')
# print(s)
# name = input('请输入名字：')
# s = '我叫{name}，今年{age}，爱好{hobby}，再说一下我叫{name}'.format(age=18,name=name,hobby='girl')
# print(s)

# s = '来看待街坊邻居复合大师街坊法好的撒见客户'
# s11 = s.replace('街坊','老王',1)
# print(s11)

# s = 'fhdsklfds'
# for i in s:
#     print(i)
s = 'fdsa苍井空fdsalk'
if '苍井空' in s:
    print('您的评论有敏感词...')