import os,time,random
from multiprocessing import Process,Pool,Manager,Queue

def p_copy(old_folder,new_folder,file,q):
    try:
        # time.sleep(random.random)
        with open(os.path.join(old_folder,file),"rb") as f:
            content=f.read()

        with open ( os.path.join ( new_folder, file ), "wb" ) as b:
            b.write(content)
    except Exception as r:
        print("出错了，原因是：%s" % r)
    else:
        print(file,"已经成功拷贝！")
        q.put(file)







if __name__ == '__main__':
    start=time.time()
    old_folder = r'..\ex'
    new_folder = "..\\new_ex"
    file_list = os.listdir ( old_folder )
    try:
        os.mkdir ( new_folder )
    except Exception as r:
        print ( "文件夹已经存在！" )
    q=Manager().Queue()
    po=Pool(3)
    for file in file_list:
        po.apply_async(p_copy,args=(old_folder,new_folder,file,q))

    po.close()
    # po.join()
    total_num = len ( file_list )
    # coped=[]
    i=0
    while 1:
        q.get()
        # print(coped)
        i=i+1
        print("\r已经拷贝了%.f %%"%(i*100/total_num))
        if i>=total_num:
            break

    end = time.time ()
    print ( "总共用时{}秒".format( (end - start) ) )
