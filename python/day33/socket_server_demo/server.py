import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.send(b'hello')    # conn
        msg = self.request.recv(1024).decode('utf-8')
        print(msg)
server = socketserver.ThreadingTCPServer(
                ('127.0.0.1',9000),
                MyServer)
server.serve_forever()