text = input('Text: ')
vowel = ['a', 'e', 'i', 'o', 'u']
check = 0
for index in text:
    if index in vowel:
        check +=1
if check > 0:
    print('There is vowel.')
else:
    print('There is not vowel.')