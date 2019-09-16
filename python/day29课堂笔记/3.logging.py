# login  登录
# log 日志
# logging

# 什么叫日志？
# 日志 用来记录用户行为 或者 代码的执行过程
# print

# logging
# 我能够“一键”控制
# 排错的时候需要打印很多细节来帮助我排错
# 严重的错误记录下来
# 有一些用户行为 有没有错都要记录下来

import logging
# logging.basicConfig(level=logging.WARNING,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S')
# try:
#     int(input('num >>'))
# except ValueError:
#     logging.error('输入的值不是一个数字')

# logging.debug('debug message')       # 低级别的 # 排错信息
# logging.info('info message')            # 正常信息
# logging.warning('warning message')      # 警告信息
# logging.error('error message')          # 错误信息
# logging.critical('critical message') # 高级别的 # 严重错误信息

# print('%(key)s'%{'key':'value'})
# print('%s'%('key','value'))

# basicconfig 简单 能做的事情相对少
    # 中文的乱码问题
    # 不能同时往文件和屏幕上输出

# 配置log对象 稍微有点复杂 能做的事情相对多
import logging
logger = logging.getLogger()
fh = logging.FileHandler('log.log',encoding='utf-8')
sh = logging.StreamHandler()    # 创建一个屏幕控制对象
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
# 文件操作符 和 格式关联
fh.setFormatter(formatter)
sh.setFormatter(formatter2)
# logger 对象 和 文件操作符 关联
logger.addHandler(fh)
logger.addHandler(sh)
logging.debug('debug message')       # 低级别的 # 排错信息
logging.info('info message')            # 正常信息
logging.warning('警告错误')      # 警告信息
logging.error('error message')          # 错误信息
logging.critical('critical message') # 高级别的 # 严重错误信息

# 程序的充分解耦
# 让程序变得高可定制

# zabbix

# logging
# 有5种级别的日志记录模式 ：
# 两种配置方式：basicconfig 、log对象

# django框架

# 作业 必须要写log







