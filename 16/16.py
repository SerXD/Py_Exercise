hour = int(input('Hour: '))
minute = int(input('Minute: '))
price = 0
if minute > 0:
    hour+=1
hour = hour-1
for i in range(hour):
    price+=30
print('Price for Parking: {} bath'.format(price))