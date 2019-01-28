import threading
import socket
def udp_send(a):
    while 1:
        send_msg=input("请输入发送内容：")
        if str(send_msg)=="q":
            print("退出发送！")
            break
        a.sendto(send_msg.encode('gbk'), ("127.0.0.1", 10000))



def udp_recv(udp_socket):
    while 1:
        recf_data = udp_socket.recvfrom(1000)
        if recf_data:
            r_msg = recf_data[0].decode("gbk")
            r_addr = recf_data[1]
            print("")
            print(r_addr, r":/t", r_msg)
        else:
            break

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    udp_socket.bind(("",7890))
    t1=threading.Thread(target=udp_recv,args=(udp_socket,))
    t2=threading.Thread(target=udp_send,args=(udp_socket,))

    t1.start()
    t2.start()
    # udp_send(udp_socket)
    # # 接收
    #
    # #发送数据
    #
    #
    # udp_recv(udp_socket)
    while 1:
        if len(threading.enumerate())<=1:
            udp_socket.close()
            break




if __name__ == '__main__':
    main()