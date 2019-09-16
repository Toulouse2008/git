import os
ret = os.urandom(32)  #生成一个32位的随机字节
print(ret)
import hmac
# 内置模块
# 简单的网络编程中的客户端合法性验证
hmac_obj = hmac.new(b'egg',ret)
ret = hmac_obj.digest()
print(ret)   # 密文的结果