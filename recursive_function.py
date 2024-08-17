time = int(input('How many time do you print: '))
for i in range(time):
    def fact(n):
        if n == 1:
            return 1
        else:
            return n * fact(n-1)

    n = int(input('Enter the factorial number: '))

    print(fact(n))











