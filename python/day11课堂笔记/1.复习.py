# 之前做得的题 以后再遇到能保证会
# 下周二考 ：所有的知识
# 面试题：认真对待
#
# 三元运算符
# 接收结果的变量 = 条件为真的结果 if 条件 else 条件为假的结果
# 接收结果的变量 = “真结果” if 条件 else “假结果”
#
# 命名空间 和 作用域
# 三种：内置 全局 局部
# 作用域：全局 局部 globals() locals()
#         global  在局部声明一个全局变量
#         nonlocal 在局部声明最近的上一层局部中的变量
# 作用域链 ： 小范围用变量的时候，先从自己的名字空间找，
#             找不到就一层一层向外层找，知道找到为止。
#             找不到就报错。
# 函数的嵌套调用和嵌套定义
#     定义在函数内部的函数不能被外界直接调用
#     内部函数可以使用外部的变量
# 函数名的本质
#     就是一串内存地址
#     可以赋值、可以作为容器类型的元素、函数的参数和返回值 —— 第一类对象

# 闭包 ： 内部函数使用外部函数的变量
def outer():
    a = 1
    def inner():
        print(a)
    return inner

i = outer()
i()




