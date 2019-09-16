import socket
sk = socket.socket()  # 买个手机
sk.connect(('127.0.0.1',8080))  # 拨号
ret = sk.recv(1024)
print(ret)
sk.send(b'byebye!')
sk.close()
