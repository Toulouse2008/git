# 3.处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕
# def check_file(filename,aim):
#     with open(filename,encoding='utf-8') as f:   #句柄 : handler,文件操作符，文件句柄
#         for i in f:
#             if aim in i:
#                 yield i
#
# g = check_file('1.复习.py','生成器')
# for i in g:
#     print(i.strip())

# 4.写生成器，从文件中读取内容，在每一次读取到的内容之前加上‘***’之后再返回给用户。
# def check_file(filename):
#     with open(filename,encoding='utf-8') as f:   #句柄 : handler,文件操作符，文件句柄
#         for i in f:
#             yield '***'+i
#
# for i in check_file('1.复习.py'):
#     print(i.strip())
