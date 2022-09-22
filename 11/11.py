thb = float(input('THB: '))
if thb <= 0:
    print("You don't have {}".format('"money !"'))
else:   
    dollar = thb/32.80
    bank_receive = dollar*0.30
    print('Dollar: {}$, Bank Receive: {} bath.'.format(dollar, bank_receive))