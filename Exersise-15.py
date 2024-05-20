number = input("Enter the number here:")
numbers = number.split()
count = 0
for i in numbers:
    count+=1
print(count)
for j in range(count):
    numbers[j] = int(numbers[j])
print(numbers)

maximum_number = numbers[0]
for k in numbers:
    if k>maximum_number:
        maximum_number=k
print(maximum_number)