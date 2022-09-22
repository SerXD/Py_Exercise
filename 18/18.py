shopping = int(input('Shopping: '))
hour = int(input('Hour: '))
minute = int(input('Minute: '))
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
