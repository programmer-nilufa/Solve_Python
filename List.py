numbers = [1,2,5,1,3,9]
negetive_numbers = [-5,-9,-1]
    #The append() method adds an item to the end of the list
"""
 numbers.append(4)
 """
    #The index() method returns the index of the specified element in the list
"""
numbers = numbers.index(5)
"""
    #The list pop() method removes the item at the specified index
"""
item = numbers.pop(2)
print(item)
print(numbers)
"""
    #The remove() method removes the first matching element
"""
numbers.remove(5)
print(numbers)
"""
    #The extend() method adds all the items of the specified iterable, such as list, tuple, dictionary, or string , to the end of a list.
"""
numbers.extend(negetive_numbers)
print(numbers)
"""
    #The clear() Removes all the elements from the list
"""
numbers.clear()
print(numbers)
"""
    #The copy() Returns a copy of the list
"""
num = numbers.copy()
print(num)
"""
    #The count() Returns the number of elements with the specified value
"""
cnt = numbers.count(1)
print(cnt)
"""
    #The insert() Adds an element at the specified position
"""
numbers.insert(2,'4')
print(numbers)
"""
    #The reverse() Reverses the order of the list
"""
numbers.reverse()
print(numbers)
"""

        #list in python
list_1 = list(('83579'))
list_2 = [5,9,8,3]
print(len(list_1))
print(type(list_1))
print(list_1)
print(list_2)
























