import random
user_Choice = int(input("0 is rock. \n1 is paper. \n2 is sessor. \nEnter Here:"))
computer_Choice = random.randint(0,2)
print("Computer Choice:")
print(computer_Choice)
if user_Choice >=3 :
    print ("Your Value is not exucute!! you lose")
else:
    if computer_Choice == user_Choice :
        print("Draw the game")
    elif user_Choice == 0 and computer_Choice == 2:
        print("You Win")
    elif user_Choice == 2 and computer_Choice == 0:
        print("You lose")
    elif user_Choice > computer_Choice :
        print("You Win")
    elif computer_Choice > user_Choice :
        print("You lose")

