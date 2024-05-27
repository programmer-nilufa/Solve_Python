import random
character = int(input("Enter how many character do you want:"))
numbers = int(input("Enter how many number do you want:"))
symbol =int(input("Enter how many symbol do you want:"))
char = ("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ")
num = ("123456789")
sym = ("!@#$%^&*~")

list=[]
for i in range(character):
    c = random.choice(char)
    list.append(c)
for i in range(numbers):
    n = random.choice(num)
    list.append(n)
for i in range(symbol):
    s = random.choice(sym)
    list.append(s)

random.shuffle(list)
x = "".join(list)
print(x)