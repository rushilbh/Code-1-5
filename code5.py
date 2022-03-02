#code5
#(Q11)
price = int(input('Enter Price -->'))

if price > 100000:
    print('Cost \/')
    print(price + (price * 15/100))
elif price > 50000 and price <= 100000:
    print('Cost \/')
    print(price + (price * 10/100))
elif price <=50000:
    print('Cost \/')
    print(price + (price * 5/100))