# import socket
# #
# #
# # def main():
# #     # 1. 买个手机(创建套接字 socket)
# #     tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #
# #     # 2. 插入手机卡(绑定本地信息 bind)
# #     tcp_server_socket.bind(("", 7890))
# #
# #     # 3. 将手机设置为正常的 响铃模式(让默认的套接字由主动变为被动 listen)
# #     tcp_server_socket.listen(128)
# #
# #     # 4. 等待别人的电话到来(等待客户端的链接 accept)
# #     new_client_socket, client_addr = tcp_server_socket.accept()
# #     print(client_addr)
# #
# #     # 5. 接收客户端发送过来的请求
# #     recv_data = new_client_socket.recv(1024)
# #     print(recv_data)
# #     response="HTTP/1.1 200 ok\r\n"
# #     response+="\r\n"
# #     response+="assssss"
# #     # 6. 回送一部分数据给客户端
# #     new_client_socket.send(response.encode("utf-8"))
# #
# #     # 7. 关闭套接字
# #     new_client_socket.close()
# #     tcp_server_socket.close()
# #
# #
# # if __name__ == "__main__":
# #     main()


def login():
    b="登陆界面"
    return b

def register():
    b="注册界面"
    return b

def quit():
    b="退出登陆"
    return b

def application(file_name):
    if file_name=="/login":
        return login()
    elif file_name=="/register":
        return register()
    elif file_name=="/quit":
        return quit()
    else:
        return "输入错误！"

