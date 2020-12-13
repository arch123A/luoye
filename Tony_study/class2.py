class Cat:
    def __init__(self):
        self.type="波斯猫"
        self.color=None
        self.name=None

cat1=Cat()
cat2=Cat()
cat3=Cat()
cat1.color='yellow and blue'
cat2.color='red and white'
cat3.color="pink"
cat1.name="大帅"
cat2.name="中帅"
cat3.name="小帅"
list1=[cat1,cat2,cat3]
for i in list1:
    print(i.name,i.color)

