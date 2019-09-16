# 2、写函数，接收n个数字，求这些参数数字的和。
def sum_func(*args):
	total = 0
	for i in args:
		total += i
	return total
print(sum_func(1,2,3,8,23,6))

# 3、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# 	a=10
# 	b=20
# 	def test5(a,b):
#      	print(a,b)
# 	c = test5(b,a)
# 	print(c)



# 4、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# 	a=10
# 	b=20
# 	def test5(a,b):
# 		a=3
# 		b=5
#      	print(a,b)
# 	c = test5(b,a)
# 	print(c)