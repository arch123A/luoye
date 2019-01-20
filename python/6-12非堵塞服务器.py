import re
import socket
import time
"""实现服务器长链接"""
def send_data(new_client_socket,request):
    """从服务器发送数据到客户端"""

    print ( ">" * 30 )
    print(request)
    head_error = "HTTP/1.1 404 OK\r\n"
    head_error += "\r\n"

    head= "HTTP/1.1 200 OK\r\n"



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

    try:
        with open ( "./dj" + file_name, "rb" ) as f:
            content = f.read ()  # content为返回的数据类型
    except Exception as ret:
        print ( ret )
        print ( type ( ret ) )

        new_client_socket.send ( head_error.encode ( "utf-8" ) )
        new_client_socket.send ( str ( ret ).encode ( "utf-8" ) )
        # new_client_socket.send ( "file not fount".encode ( "utf-8" ) )

    else:
        head += "Content-Length:%d\r\n" % len ( content ) # Content-Length为接受浏览器接受的长度，以实现长链接
        head += "\r\n"  # head为头文件
        new_client_socket.send ( head.encode ( "utf-8" ) )
        new_client_socket.send ( content )




if __name__ == '__main__':
    tcp_socket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    tcp_socket.setsockopt ( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    # 这里value设置为1，表示将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
    tcp_socket.setblocking(False)  # 设置套接字为非堵塞
    addr = ("", 8888) # 绑定端口号
    tcp_socket.bind ( addr )
    tcp_socket.listen ( 128 )
    client_socket_list=[]
    while True:
        time.sleep(0.5)
        try:
            new_client_socket, client_addr = tcp_socket.accept ()
        except Exception as reason:
            print("——————没有客户端到来")
        else:
            print("——————来了一个新的客户端")
            new_client_socket.setblocking ( False )
            client_socket_list.append(new_client_socket)

        for client_socket in client_socket_list:
            print(">"*30)
            print(len(client_socket_list))
            try:
                request = client_socket.recv ( 1024 )
            except:
                print("》》》》》有客户端，但没有接受到数据")
            else:
                print("》》》》》接受到新的数据")

                if request:
                    send_data(client_socket,request)
                else:
                    client_socket_list.remove(client_socket)
                    client_socket.close()
    tcp_socket.close ()



