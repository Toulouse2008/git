import os
import socket
import hashlib
def check_client(conn):
    secret_key = b'egg'  # 密钥
    send_str = os.urandom(32)
    conn.send(send_str)
    md5_obj = hashlib.md5(secret_key)
    md5_obj.update(send_str)
    secret_ret = md5_obj.hexdigest()
    if conn.recv(1024).decode('utf-8') == secret_ret:
        print('合法的客户端')
        return   True
    else:
        print('非法的客户端')
        return   False


sk = socket.socket()
sk.bind(('127.0.0.1',8090))
sk.listen()

conn,addr = sk.accept()
ret = check_client(conn)
while ret:
    inp = input('>>>')
    conn.send(inp.encode('utf-8'))
    msg = conn.recv(1024)
    print(msg.decode('utf-8'))
conn.close()
sk.close()
