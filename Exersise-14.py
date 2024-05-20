# height = input("Enter the heights value:")
# height_list = height.split()
#
# count = 0
# for heights in height_list:
#     count = count+1
# print(count)
# for i in range(0,count):
#     height_list[i] = int(height_list[i])
# print(height_list)
#
# total = 0
# for person in height_list:
#     total+=person
# avg = total/count
# print(round(avg))


heights = input("Enter the element:")
height_list = heights.split()

count = 0
for height in height_list:
    count+=1
print(count)

for i in range(0,count):
    height_list[i] = int(height_list[i])
print(height_list)

total = 0
for person in height_list:
    total+=person
avg = total/count
print(round(avg))

























