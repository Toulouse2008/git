import socket
sk = socket.socket()
# sk.setblocking(False)
# sk.settimeout(5)
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()  # 阻塞
conn.send(b'gskjldfgkasdg')
print('getpeername : \n',conn.getpeername())   #连接到当前套接字的远端的地址
print('getsockopt : \n',sk.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR))      #返回指定套接字的参数
conn.recv(1024)  # 阻塞
# conn.sendall(b'gskjldfgkasdg')
conn.close()
sk.close()