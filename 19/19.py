shopping = int(input('Shopping: '))
hour = int(input('Hour: '))
minute = int(input('Minute: '))
if shopping or hour or minute < 0 :
    print("It can't be negative.")
else:
    price = 0
    if shopping >= 1000:
        hour-=4
    else:
        hour-=1
    if minute > 0:
        hour+=1
    for index in range(hour):
        price+=30
    print('Price Parking: {} bath.'.format(price))
