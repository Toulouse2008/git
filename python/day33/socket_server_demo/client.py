# tcp
    # 粘包
    # 在同一时间只能处理一个客户端的请求
import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
print(sk.recv(1024))
msg = input('>>>').encode('utf-8')
sk.send(msg)
sk.close()