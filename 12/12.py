number = int(input('Number: '))
if number == 0:
    print('zero.')
elif number > 0:
    if number%2 == 0:
        print('Positive Even.')
    else:
        print('Positive Odd.')
else:   
    if number%2 == 0:
        print('Negative Even.')
    else:
        print('Negative Odd.')