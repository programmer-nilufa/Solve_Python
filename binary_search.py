size = int(input('Enter list size: '))

list = []
for i in range(size):
    item = int(input('Enter the item: '))
    list.append(item)

print('Before sorted = ',list)

list_item = sorted(list)
print('After sorted = ',list_item)

key_item = int(input('Enter the search item: '))
start = 0
end = len(list_item)-1

while(start<=end):
    mid = (start+end)//2
    if list_item[mid] == key_item:
        print(f'Your search item is {mid} index')
        break
    elif list_item[mid] < key_item:
        start = mid+1
    elif list_item[mid] > key_item:
        end = mid-1
    else: print('Your data not found')

