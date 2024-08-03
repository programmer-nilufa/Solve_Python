print('Search the value is number 6')
list = [4,5,9,1,6,2]      #[1,2,4,5,6,9]
print('The sorted number is',sorted(list))
list_mod = sorted(list)
start = 0
end = 5
mid = (start+end)//2
mid_item = list_mod[mid]

print(f'Start number is {start} index, End number is {end} index, Mid number is {mid} index')
print(f'The value of mid {mid_item}')

for i in range(len(list)):
    if mid_item == 6:
        print('Your value here')
    else:print('Your value is not founded')


start = mid
end = 5
mid = (start+end)//2
mid_item = list_mod[mid]

print(f'Start number is {start} index, End number is {end} index, Mid number is {mid} index')
print(f'The value of mid {mid_item}')

for i in range(len(list)):
    if mid_item == 6:
        print('Your value here')
    else:print('Your value is not founded')

start = mid
end = 5
mid = (start + end) // 2
mid_item = list_mod[mid]

print(f'Start number is {start} index, End number is {end} index, Mid number is {mid} index')
print(f'The value of mid {mid_item}')

for i in range(len(list)):
    if mid_item == 6:
        print('Your value here')
    else:
        print('Your value is not founded')

