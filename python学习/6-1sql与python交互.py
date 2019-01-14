from pymysql import connect
def query_data(sql):
    con=connect(host='localhost',port=3306,user='root',password='123456',database="jing_dong",charset="utf8")
    cs=con.cursor()
    cs.execute(sql)
    a=cs.fetchall()

    for i in a:
        print(str(i))

    cs.close()
    con.close()

def modify_data(sql):
    con=connect(host='localhost',port=3306,user='root',password='123456',database="jing_dong",charset="utf8")
    cs=con.cursor()
    cs.execute(sql)
    con.commit()
    cs.close()
    con.close()

class Jd():
    def __init__(self):
        self.con = connect ( host='localhost', port=3306, user='root',
                             password='123456', database="jing_dong",
                             charset="utf8" )
        self.cursor=self.con.cursor()

    def __del__(self):
        self.cursor.close()
        self.con.close()

    def execute(self,sql):
        self.cursor.execute ( sql )
        for i in self.cursor.fetchall ():
            print ( i )

    def show_all(self):
        sql="""select * from goods;"""
        self.execute(sql)

    def show_brand(self):
        sql="""select distinct brand_name from goods;"""
        self.execute(sql)

    def show_type(self):
        sql = """select cate_name from goods group by cate_name;"""
        self.execute ( sql )

    @staticmethod
    def print_menu():
        print ( "1.显示所有商品" )
        print ("2.显示所有品牌分组" )
        print ("3.显示所有商品各类" )
        print("")
        return input ( "请输入所需要的功能：" )

    def run(self):

        num=self.print_menu()

        if num == "1":
            self.show_all()
        elif num=="2" :
            self.show_brand()
        elif num=="3" :
            self.show_type()
        else:
            print("输入错误！")




if __name__ == '__main__':
   jd=Jd()

   while 1:
        jd.run()
