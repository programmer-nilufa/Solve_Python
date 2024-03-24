# import random
# n = int(input("Enter the number: "))
# if n%2 == 0:
#     n = random.randrange(2,5)
#     print("Not Weird")
#     n = random.randrange(6, 20)
#     print("Weird")
#     if n>20:
#         print("Not Weird")
# else:
#     print("Weird")



n = int(input())

if n%2!= 0:
    print("Weird")
else:
    if (n>=2 and n<=5):
        print("Not Weird")
    elif (n>=6 and n<=20):
        print("Weird")
    else:
        print("Not Weird")

















