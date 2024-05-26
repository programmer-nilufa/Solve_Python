a = range(1,101)
for i in a:
    if i%3==0 and i%5==0:
        print("fizzBuzz")
    elif i%5==0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)

