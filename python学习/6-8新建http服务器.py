
import socket
def send_data(new_client_socket):
    """从服务器发送数据到客户端"""

    request = new_client_socket.recv(1024)
    print(request)

    a = "HTTP/1.1 200 OK\r\n"
    response=a+"\r\n"+"\r\n"+"<h1>index2</h1>"
    new_client_socket.send(response.encode("utf-8"))

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



