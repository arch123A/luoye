
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


