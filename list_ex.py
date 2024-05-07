list_1 = [1,1,1]
list_2 = [1,1,1]
list_3 = [1,1,1]
list = [list_1,list_2,list_3]

print(f"{list_1}\n{list_2}\n{list_3}")

position = input("Enter your position where you want hide your money: ")

row = int(position[0])
coloum = int(position[1])

list[row-1][coloum-1] = "X"
print(f"{list_1}\n{list_2}\n{list_3}")
