import json
import hashlib
import socketserver
def md5_pwd(user,pwd):
    md5_obj = hashlib.md5(user.encode('utf-8'))
    md5_obj.update(pwd.encode('utf-8'))
    ret = md5_obj.hexdigest()
    return ret

def login(userinfo):
    user_dic = json.loads(userinfo)
    passwd = md5_pwd(user_dic['username'], user_dic['passwd'])
    with open('userinfo') as f:
        for line in f:
            user, pwd = line.split('|')
            if user_dic['username'] == user and passwd == pwd:
                print('登录成功')
                break

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        userinfo = self.request.recv(1024).decode('utf-8')
        login(userinfo)

server = socketserver.ThreadingTCPServer(
                ('127.0.0.1',9000),
                MyServer)
server.serve_forever()