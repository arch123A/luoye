import threading
import socket


#发送数据功能
def send_msg(udp_socket, send_address):
    while True:
        send_msg = input("发送")
        udp_socket.sendto(send_msg.encode("utf-8"), send_address)
        if send_msg == "exit":
            break


#显示数据功能
def display_msg(udp_socket):
    while True:
        recv_data, ip_port = udp_socket.recvfrom(1024)
        if recv_data:
            print(recv_data.decode("utf-8"), "接收到到信息",ip_port)

if __name__ == "__main__":
    #创建udp套接字进行连接
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 9090))
    send_address = ("25 .26 .109.11 ", 10000)
    #创建子线程执行数据发送功能
    send_msg_thread = threading.Thread(target=send_msg, args=(udp_socket, send_address))
    send_msg_thread.start()
    #主线程执行数据接收和展示功能
    display_msg(udp_socket)
