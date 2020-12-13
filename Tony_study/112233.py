class Phone:
    def __init__(self):
        self.power=100
    def game(self):
        print('正在打游戏')
        self.power-=10
    def music(self):
        print("正在听歌")
        self.power-=5
    def call(self):
        print("正在打电话")
        self.power-=4
    def answer(self):
        print("正在接电话")
        self.power-=3
    def charge(self,num):
        print("正在充电，充电量是%d"%num)
        self.power+=num

    def __str__(self):
         return "当前手机电量为：%d"% self.power

p=Phone()
p.game()
p.music()
print(p)