a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a
print(a is b)
print(a is c)

print(a is not b)
print(a is not c)

print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))