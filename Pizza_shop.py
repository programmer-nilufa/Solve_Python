Order = int(input("Which type pizza: \n1.Small Pizza \n2.Middium Pizza \n3.Large Pizza \nEnter Here: "))
if Order==1:
    price = 200

    paparoni = int(input("Do you want extra paparoni?\n1.Yes \n2.No \nEnter Here: "))
    if paparoni == 1:
        price = price+20

        chess = int(input("Do you want extra chess?\n1.Yes \n2.No \nEnter Here: "))
        if chess == 1:
            price = price+20
            print("Your bill:",price)
        else:
            print("Your bill:",price)
    else:

        chess = int(input("Do you want extra chess?\n1.Yes \n2.No \nEnter Here: "))
        if chess == 1:
            price = price + 20
            print("Your bill:",price)
        else:
            print("Your bill:",price)
elif Order==2:
    price = 300
    paparoni = int(input("Do you want extra paparoni?\n1.Yes \n2.No \nEnter Here: "))
    if paparoni == 1:
        price = price+20

        chess = int(input("Do you want extra chess?\n1.Yes \n2.No \nEnter Here: "))
        if chess == 1:
            price = price+20
            print("Your bill:",price)
        else:
           print("Your bill:",price)
    else:

        chess = int(input("Do you want extra chess?\n1.Yes \n2.No \nEnter Here: "))
        if chess == 1:
            price = price + 20
            print("Your bill:",price)
        else:
            print("Your bill:",price)
elif Order==3:
    price = 300
    paparoni = int(input("Do you want extra paparoni?\n1.Yes \n2.No \nEnter Here: "))
    if paparoni == 1:
        price = price+30

        chess = int(input("Do you want extra chess?\n1.Yes \n2.No \nEnter Here: "))
        if chess == 1:
            price = price+20
            print("Your bill:",price)
        else:
            print("Your bill:", price)
    else:

        chess = int(input("Do you want extra chess?\n1.Yes \n2.No \nEnter Here: "))
        if chess == 1:
            price = price + 20
            print("Your bill:",price)
        else:
            print("Your bill:",price)