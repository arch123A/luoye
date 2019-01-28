import re
import socket
def send_data(new_client_socket):
    """从服务器发送数据到客户端"""

    request = new_client_socket.recv(1024)
    print(request)
    print(">"*30)
    a = "HTTP/1.1 200 OK\r\n"
    head=a+"\r\n"  # head为头文件

    if request:
        request_line=request.splitlines()[0]

        print(request_line)
        res = re.search ( r'[^/]+(/[^ ]*?) ', request_line.decode("utf-8") )

        file_name=res.group(1)
        print(file_name)
    if file_name=="/":
        file_name="/index.html"

       

    try:
        with open("./dj"+file_name,"rb") as f:
            content = f.read ()  # content为返回的数据类型
    except Exception as ret:
        print(ret)
        print(type(ret))
        head="HTTP/1.1 404 OK\r\n"
        head+="\r\n"
        new_client_socket.send ( head.encode ( "utf-8" ) )
        new_client_socket.send (str(ret).encode("utf-8"))
        new_client_socket.send ("file not fount".encode("utf-8"))

    else:
        new_client_socket.send ( head.encode ( "utf-8" ) )
        new_client_socket.send ( content)





    new_client_socket.close()


if __name__ == '__main__':
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 这里value设置为1，表示将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。

    addr=("",8888)
    tcp_socket.bind(addr)
    tcp_socket.listen(128)

    while True:
        new_client_socket, client_addr = tcp_socket.accept()
        print(client_addr)
        send_data(new_client_socket)

    tcp_socket.close()



