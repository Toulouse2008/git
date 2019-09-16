import socket
sk = socket.socket()  # 创建了一个socket对象
sk.bind(('192.168.21.36',8080))  # 绑定一台机器的(ip,端口)
# 回环地址 - 指向自己这台机器
sk.listen()    # 建立监听等待别人连接
conn,addr = sk.accept()       # 阻塞:在这里等待直到接到一个连接
# conn是连接
# addr是对方的地址
print(conn)
print(addr)
conn.send(b'hello')              # 和对方打招呼
msg = conn.recv(1024)                 # 对方和我说的话
# 有发必有收 收发必相等
print(msg)
conn.close()                      # 挂电话
sk.close()                        # 关机
