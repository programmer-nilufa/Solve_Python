number = input("Enter the number:")
numbers = number.split()

count = 0
for i in numbers:
    count+=1
print(count)

for i in range(count):
    numbers[i]=int(numbers[i])
print(numbers)

minimum = numbers[0]
for j in numbers:
    if j<minimum:
        minimum=j
print(minimum)