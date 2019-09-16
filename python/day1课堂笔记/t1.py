#-*- encoding:utf-8 -*-
#print('我爱中国')
'''
x = 1+2+3+4
print(x)
print(x*5)
y = x*5
print(y+100-45+2)

print('泰哥泰哥，我是小弟')
print('泰哥泰哥，我是三弟小妹')


t-t = 2
3t_t = 23
*r = 4
_ = 'fdsa'
___ = 4
%- = 'fdsa'
2w = 5
qwe-r = 'wer'

kfdsdlafhsdakfhdsakdfjkhsdakf = '太白'
print(名字)
AgeOfOldboy = 56

NumberOfStudents = 80

#下划线

age_of_oldboy = 56

number_of_students = 80


age1 = 12 
age2 = age1
age3 = age2
age2 = 100
age3 = 5
print(age1,age2,age3) #12, 100 ,100
					  #12,12,12,
					  #12,100,12
					  #100,100,100,

print(100,type(100))
print('100',type('100'))

print(1)
print("jsdfdsfsadl;fjdsal;j")
print("I'm a teacher")


a = '泰哥'
b = '小二'
c = a + b
print(c)
print('泰哥' + '小二' +'货')

print('坚强'*8)


msg = """
今天我想写首小诗，
歌颂我的同桌，
你看他那乌黑的短发，
好像一只炸毛鸡。
"""
#print(msg)
print(True,type(True))
print('True',type('True'))

name = input('请输入你的名字：')
age = input('请输入你的年龄：')
print('我的名字是'+name,'我的年龄'+age+'岁')
'''
#第一种：
'''
if 4 > 5 :
	print('我请你喝酒')
print('喝什么酒')

#第二种：
if 4 > 5:
	print('我请你喝酒')
else:
	print('喝什么酒')
'''

'''
#多选：
num = input('请输入您猜的数字：')

if num == '1':
	print('一起抽烟')
elif num == '2':
	print('一起喝酒')
elif num == '3':
	print('新开了一家，走看看')
else:
	print('你猜错了.....')


score = int(input("输入分数:"))

if score > 100:
    print("我擦，最高分才100...")
elif score >= 90:
    print("A")
elif score >= 60:
    print("C")
elif score >= 80:
    print("B")
elif score >= 40:
    print("D")
else:
    print("太笨了...E")

name = input('请输入名字：')
age = input('请输入年龄：')

if name == '小二':
	if age == '18':
		print(666)
	else:
		print(333)
else:
	print('错了....')
'''


#while
'''
print('111')
while True:
	print('我们不一样')
	print('在人间')
	print('痒')
print('222')
'''
#从1--100 
'''
count = 1
flag = True
#标志位
while flag:
	print(count)
	count = count + 1
	if count > 100 :
		flag = False


count = 1
while count <= 100:
	print(count)
	count = count + 1


count = 1
sum = 0

while count <= 100:
	sum = sum + count 
	count = count + 1
	
print(sum)
'''

#break
'''
print('11')
while True:
	print('222')
	print(333)
	break
	print(444)
print('abc')

count = 1
while True:
	print(count)
	count = count + 1
	if count > 100:break




print(111)
count = 1
while count < 20 :
	print(count)
	continue
	count = count + 1
'''
	
count = 0
while count <= 100 : 
    count += 1
    if count > 5 and count < 95: 
        continue 
    print("loop ", count)

print("-----out of while loop ------")
	






