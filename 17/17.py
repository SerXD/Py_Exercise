Hour = int(input('Hour: '))
Minute = int(input('Minute: '))
if Hour < 0 or Minute < 0 :
    print("It can't be negative")
else:
    Hour = Hour-1
    if Minute > 0:
        Hour+=1
    if Hour == -1:
        bath = 0
    else: 
        bath = Hour*30
    print('Price Parking: {} bath.'.format(bath))
