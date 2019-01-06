import socket
def send():
    udp1 = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM )
    local_addr = ("", 9989)
    udp1.bind ( local_addr )
    while 1:
        # print("开始发送消息…………")
        data_send=input("请输入发送的内容：")
        udp1.sendto(data_send.encode('gbk'),("127.0.0.1",12121))



if __name__ == '__main__':
    send()