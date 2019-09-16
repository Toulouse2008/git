def qqxing(k,l = {}):
    # l.append(1)
    l[k] = 'v'
    print(l)

qqxing(1)     #[1]
qqxing(2)     #[1,1]
qqxing(3)     #[1,1,1]

# 如果默认参数的值是一个可变数据类型，
# 那么每一次调用函数的时候，
# 如果不传值就公用这个数据类型的资源
