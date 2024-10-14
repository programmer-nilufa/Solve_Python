print('sat = 1, sun = 2, mon = 3, tues = 4, wed = 5, thus = 6, friday = 7')
days = int(input('Enter a day number: '))
age = int(input('Enter your age: '))
if days==5:
    if age < 18:
        discount = 8 - 2
        print(f'Your ticket price is ${discount} ')
    else:
        discount = 12 -2
        print(f'Your ticket price is ${discount} ')
else:
    if age<18:
        print('Your ticket price is $8 ')
    else:
        print('Your ticket price is $12 ')