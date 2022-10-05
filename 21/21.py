shopping = int(input('Shopping: '))
hour = int(input('Hour: '))
minute = int(input('Minute: '))
if (shopping < 0 or hour < 0 or minute < 0) :
    print("It can't be negative.")
else:
    price = 0
    if hour >= 3 :
        if minute > 0:
            hour+=1
        hour-=3
    elif hour >= 1:
        if minute > 0:
            hour+=1
        hour-=1
    for index in range(hour):
        price+=40
    if price >= 160:
        print('Price Parking: 150 bath.')
    else:
        print('Price Parking: {} bath.'.format(price))

