import random
text = input('Text: ')
if text.lower() == 'a':
    print(random.randint(80,100))
elif text.lower() == 'b':
    print(random.randint(70, 79))
elif text.lower() == 'c':
    print(random.randint(60, 69))
elif text.lower() == 'd':
    print(random.randint(50, 59))
elif text.lower() == 'f':
    print(random.randint(0, 49))
else:
    print('try again.')