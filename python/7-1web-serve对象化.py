import re
import socket
import gevent
from gevent import monkey
from python.aa import application

monkey.patch_all()

class WSGI_server():
    def __init__(self):
        self.tcp_socket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        self.tcp_socket.setsockopt ( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
        # 这里value设置为1，表示将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
        addr = ("", 8888)
        self.tcp_socket.bind ( addr )
        self.tcp_socket.listen ( 128 )
        



    def send_data(self,new_client_socket):
        """从服务器发送数据到客户端"""
    
        request = new_client_socket.recv ( 1024 )
        print ( request )
        print ( ">" * 30 )
        head_error = "HTTP/1.1 404 OK\r\n"
        head_error += "\r\n"
        file_name=""
    
        if request:
            request_line = request.splitlines ()[0]
            print ( request_line )
            res = re.search ( r'[^/]+(/[^ ]*?) ', request_line.decode ( "utf-8" ) )
            file_name=""
            if res:
                file_name = res.group (1)
                print ( file_name )
        if file_name == "/":
            file_name = "/index.html"

        if not file_name .endswith(".py"):
            try:
                with open ( "./dj" + file_name, "rb" ) as f:
                    content = f.read ()  # content为返回的数据类型
            except Exception as ret:
                print ( ret )
                print ( type ( ret ) )
                head2="HTTP/1.1 200 OK\r\n"
                head2+="\r\n"
                new_client_socket.send (head2.encode ( "utf-8" ) )
                new_client_socket.send ( str ( ret ).encode ( "utf-8" ) )
                # new_client_socket.send ( "file not fount".encode ( "utf-8" ) )

            else:
                new_client_socket.send ( head_error.encode ( "utf-8" ) )
                new_client_socket.send ( content )
        else:
            env=dict()
            env['path']= file_name
            body=application(env,self.set_response_header)
            head = "HTTP/1.1 %s\r\n" % self.status
            for t in self.header:
                head += "%s:%s\r\n" % (t[0], t[1])
                print(t)
            head += "\r\n"  # head为头文件
            print(">"*10,head)
            # print(">"*10,self.header,type(self.header))
            response=head+body
            new_client_socket.send ( response.encode("utf-8") )
        new_client_socket.close ()

    def set_response_header(self,status,header):
        self.status=status
        self.header=header

    def run(self):
        while True:
            new_client_socket, client_addr = self.tcp_socket.accept ()
            t1 = gevent.spawn (self.send_data, new_client_socket )
            t1.start ()
            # new_client_socket.close()
            print ( client_addr )



    def __del__(self):
        self.tcp_socket.close ()




if __name__ == '__main__':
    web_server=WSGI_server()
    web_server.run()