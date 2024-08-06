# list = [1,-3,5,6,-2,-6,9]
# count = 0
# for i in list:
#     if i > 0:
#         count+=1
#
# print('Positive number is:',count)


n = int(input('Enter the number: '))
number = []
for i in range(n):
    num = int(input('Enter the value here:'))
    number.append(num)
print('The value is: ',number)

positive_count_num = 0
for j in number:
    if j > 0:
        positive_count_num += 1
print('The positive number is: ',positive_count_num)




















