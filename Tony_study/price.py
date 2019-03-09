price = float(input('请输入总价:'))
member = input('请输入你是不是会员:')
if price>=100:
    price-=50
elif price>=50:
    price-=20
elif price>=30:
    price-=10
if member=='是':
    price*=0.8

print(price)
