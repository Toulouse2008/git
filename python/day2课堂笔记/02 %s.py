#格式化输出
# % s d
# name = input('请输入姓名')
# age = input('请输入年龄')
# height = input('请输入身高')
# msg = "我叫%s，今年%s 身高 %s" %(name,age,height)
# print(msg)
"""
name = input('请输入姓名:')
age = input('请输入年龄:')
job = input('请输入工作:')
hobbie = input('你的爱好:')

msg = '''------------ info of %s -----------
Name  : %s
Age   : %d
job   : %s
Hobbie: %s
------------- end -----------------''' %(name,name,int(age),job,hobbie)
print(msg)
"""
name = input('请输入姓名')
age = input('请输入年龄')
height = input('请输入身高')
msg = "我叫%s，今年%s 身高 %s 学习进度为3%%s" %(name,age,height)
print(msg)