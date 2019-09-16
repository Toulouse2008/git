import socket
sk = socket.socket()

sk.connect(('127.0.0.1',9000))

ret = sk.recv(1024)
print(ret)
sk.send(b'hahaha')
sk.close()