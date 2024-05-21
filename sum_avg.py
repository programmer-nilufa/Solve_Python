height = int(input("Count the element number:"))
list = []
for i in range(0,height):
    element = int(input(f"Enter the {i} element list here:"))
    list.append(element)
print(list)

sum = 0
for j in list:
    sum+=j
avg = sum/element
print(round(avg))





















