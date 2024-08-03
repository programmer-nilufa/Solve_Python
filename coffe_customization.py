coffe_size = input('Enter your coffe size:')
coffe_size = coffe_size.lower()
extra_shot = bool(input('Do you want extra shot? \nIf no then skip the part (enter)'))
if extra_shot:
    coffe = coffe_size + ' Coffe with an extra shot'
else:
    coffe = coffe_size + ' Coffe'

print('Order:',coffe)