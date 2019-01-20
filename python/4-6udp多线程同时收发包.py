import threading
import time

import socket

def send(udp_socket):
    # 发信息
    while 1:
        msg = input ( "请输入发送信息：" )
        udp_socket.sendto ( msg.encode ( "gbk" ), ("127.0.0.1", 10000) )


def recv(udp_socket):
    # 接受信息
    while 1:
        re_msg = udp_socket.recvfrom ( 1024 )
        print ( re_msg[0].decode("gbk"))

if __name__ == '__main__':

    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # udp_socket = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM )
    local_address=("",9999)
    udp_socket.bind(local_address)
    t1=threading.Thread(target=send,args=(udp_socket,))
    t2=threading.Thread(target=recv,args=(udp_socket,))
    t1.start()
    t2.start()