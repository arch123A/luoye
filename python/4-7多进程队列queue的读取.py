from multiprocessing import Queue,Process

def down_data(q):
    a=[11,22,33,44,55]
    for i in a:
        q.put(i)

    print("已经下完数据到队列了。")


def analysis(q):
    b=[]
    while not q.empty():
        b.append(q.get())
    print(str(b))


if __name__ == '__main__':
    q=Queue(10)
    p1=Process(target=down_data,args=(q,))
    p2=Process(target=analysis,args=(q,))
    p1.start()
    p2.start()

