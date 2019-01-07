import socket
def send_to_server():
    #  客户端连接到服务器，然后发送数据。
    tcp_socket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    local_addr = ("", 9989)
    tcp_socket.bind ( local_addr )  # 绑定的本地地址
    #连接的服务器地址
    server_addr = ("127.0.0.1", 37373)
    tcp_socket.connect(server_addr)
    while True:
        send_data=input("请输入信息：")
        tcp_socket.send(send_data.encode("gbk"))


    tcp_socket.close()

def serve():
    tcp_serve_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_serve_socket.bind(("",9990))
    tcp_serve_socket.listen(100)
    while 1:
        print("等待新的客户…………")
        new_client_socket, client_addr = tcp_serve_socket.accept ()
        print('新客户端的网址是：',client_addr)
        while True:
            recv_data=new_client_socket.recv(1024)
            if recv_data:
                print("客户端的消息是：",recv_data.decode("gbk"))
                new_client_socket.send("服务器的回复,\n".encode("gbk"))
            else:
                print("客户端已经结束！")
                break
        new_client_socket.close()
    tcp_serve_socket.close()

if __name__ == '__main__':
    serve()





