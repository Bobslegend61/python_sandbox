# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

x = 5  # int
print(type(x))

name = 'Alabi'  # String
print(type(name))

y = 5.5  # float
print(type(y))

z = 1j  # complex
print(type(z))

names = ['Gift', 'Grace', 'Brad']  # list
print(type(names))

fruits = ('Mango', 'Orange', 'Lemon')  # tuple
print(type(fruits))

j = range(6)  # range
print(type(j))

user = {
    'first_name': 'Brad',
    'last_name': 'Traversy'
}  # dict

print(type(user))

carModels = {'Benz', 'Toyota', 'Honda'}  # set
print(type(carModels))

drinks = frozenset({'Pepsi', 'Coca-cola'})  # frozenet
print(type(drinks))

isEmpty = True  # bool
print(type(isEmpty))

h = b'Hello'  # byte
print(type(h))

k = bytearray(5)  # bytearray
print(type(k))

m = memoryview(bytes(5))  # memoryview
print(type(m))
