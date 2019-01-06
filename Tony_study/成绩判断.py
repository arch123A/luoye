while True:
    a=input("请输入你的成绩：")
    print("你的成绩是%s"%(a))
    if not a.isdigit():
        print("请输入正确的数字")
        continue
    a=int(a)

    if a<60:
        print('成绩不及格。')
    elif a<80:
        print('你的成绩优良')
    elif a<100:
        print('成绩很优秀')
    elif a==100:
       print('成绩超级超级棒哦！')
    else:
        print("您输入成绩不正确")