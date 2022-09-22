number = int(input('Int: '))
if number < 0 :
    print('Please insert the number that is greater or equal zero.')
else:
    if number >= 80:
        print('A')
    elif number >= 70:
        print('B')
    elif number >= 60:
        print('C')
    elif number >= 50:
        print('D')
    else:
        print('F')
