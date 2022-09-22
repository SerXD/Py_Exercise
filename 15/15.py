number_1 = int(input('Number 1: '))
number_2 = int(input('Number 2: '))
if number_1+number_2 > 0 :
    if (number_1+number_2)%2 == 0:
        print('Positive Even')
    else:
        print('Positive Odd')
elif number_1+number_2 < 0 :
    if (number_1+number_2)%2 == 0:
        print('Nagetive Even')
    else:
        print('Nagetive Odd')
else:
    print('Zero.')