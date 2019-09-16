import socket
import hashlib
sk = socket.socket()
sk.connect(('127.0.0.1',8090))

recv = sk.recv(1024)
# 用和server端相同的手法对这个字符串进行摘要
secret_key = b'egon'  # 密钥
md5_obj = hashlib.md5(secret_key)
md5_obj.update(recv)
ret = md5_obj.hexdigest()
sk.send(ret.encode('utf-8'))
msg = sk.recv(1024)
if msg:
    print(msg.decode('utf-8'))
    while True:
        inp = input('>>>')
        sk.send(inp.encode('utf-8'))
        msg = sk.recv(1024)
        print(msg.decode('utf-8'))
sk.close()