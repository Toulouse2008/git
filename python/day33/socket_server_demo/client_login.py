import json
import socket
ADDR = ('127.0.0.1',9000)
def get_socket():
    sk = socket.socket()
    sk.connect(ADDR)
    return sk
# 输入账号
username = input('username >>>')
passwd = input('password >>>')
if username.strip() and passwd.strip():
    sk = get_socket()
    dic = {'username':username,'passwd':passwd}
    str_dic = json.dumps(dic)
    sk.send(str_dic.encode('utf-8'))
sk.close()
# 连接socket