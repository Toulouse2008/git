'''
3、元素分类
    有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}


'''
# li= [11,22,33,44,55,66,77,88,99,90]
# dic ={}
# l_greater=[] #大于66的所有值列表
# l_less=[]    #小于66的所有值列表
# for i in li:
#     if i == 66:continue
#     if i > 66 :
#         l_greater.append(i)
#     else :
#         l_less.append(i)
# dic.setdefault('k1',l_greater)
# dic.setdefault('k2',l_less)
# print(dic)

'''
4、输出商品列表，用户输入序号，显示用户选中的商品
    商品 li = ["手机", "电脑", '鼠标垫', '游艇']
要求：1：页面显示 序号 + 商品名称，如：
      	1 手机
	   	2 电脑
     		 …
     2： 用户输入选择的商品序号，然后打印商品名称
  3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。

'''
# flag = True
# while flag:
#     li = ["手机", "电脑", "鼠标垫", "游艇"]
#     for i in li:
#         print('{}\t\t{}'.format(li.index(i)+1,i))
#     num_of_chioce = input('请输入选择的商品序号/输入Q或者q退出程序：')
#     if num_of_chioce.isdigit():
#         num_of_chioce = int(num_of_chioce)
#         if num_of_chioce > 0 and num_of_chioce <= len(li):
#             print(li[num_of_chioce-1])
#         else:print('请输入有效数字')
#     elif num_of_chioce.upper() == 'Q':break
#     else:print('请输入数字')
