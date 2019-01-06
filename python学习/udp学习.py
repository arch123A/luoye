import socket
#接收数据
def recv(udp_socket):
    print("开始接受数据…………")
    recf_data=udp_socket.recvfrom(1000)
    r_msg=recf_data[0].decode("gbk")
    r_addr=recf_data[1]
    print(r_addr,r":/t",r_msg)



def send(udp_socket):
    print("开始发送消息…………")
    data_send=input("请输入发送的内容：")
    udp_socket.sendto(data_send.encode('gbk'),("127.0.0.1",10000))

def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("", 12121))

    while 1:
        send(udp_socket)
        recv(udp_socket)
    udp_socket.close()


if __name__ == '__main__':
    main()