shopping = int(input('Shopping: '))
hour = int(input('Hour: '))
minute = int(input('Minute: '))
if shopping >= 1000:
    hour-=4
else:
    hour-=1
if minute > 0:
    hour+=1
if hour < 0:
    price = 0
else:
    price = hour*30
print('Price Parking: {} bath.'.format(price))
