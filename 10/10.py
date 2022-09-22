dollar = int(input('Dollar: '))
if dollar <= 0:
    print("You don't have money.")
else: 
    thb = dollar*32.5
    print('THB: {}'.format(thb))