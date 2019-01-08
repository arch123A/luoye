import socket
def send2server_down_file():

    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    local_addr=("",9899)
    tcp_socket.bind(local_addr)
    tcp_socket.connect(("127.0.0.1",9000))

    msg=input("输入文件名:")
    tcp_socket.send(msg.encode("gbk"))
    recv_data=tcp_socket.recv(1024)
    print(recv_data.decode("gbk"))
    if recv_data:
        with open("new"+msg,"wb") as f :
            f.write(recv_data)
            print("已经保存完毕！")
    # 关闭套接口
    tcp_socket.close()

def server():
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    local_addr=("",9000)
    tcp_socket.bind(local_addr)
    tcp_socket.listen(128)
    new_client_socket,client_addr=tcp_socket.accept()
    print(client_addr)
    client_msg=new_client_socket.recv(1024)
    filename=client_msg
    content=None
    try:
        f=open(filename,"rb")
        content=f.read()
        f.close()
    except OSError as r:
        print("打开文件出错了,原因是：", r)


    if content:
        new_client_socket.send(content)
        print("发送成功")

    else:
        print("发送失败。")
    new_client_socket.close()
    tcp_socket.close()


if __name__ == '__main__':
    server()