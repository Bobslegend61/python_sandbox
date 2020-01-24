# single line strig
name = 'Alabi'
print(name)

# multiline string
sentence = '''This is a sentense
and the sentences
continues from
here.
'''

print(sentence)

# Strings are arrays
a = 'Hello, World'
print(a[0])


# slice syntax
print(a[2:5])

print(a[-5:-2])

# length
print(len(a))

# STRING METHODS

# strip - acts like trim in JS
print(a.strip())

# lowercase
print(a.lower())

# uppercase
print(a.upper())

# Replace
print(a.replace('H', 'J'))

# Split
print(a.split(','))

# check string
print('o' in a)

print('h' not in a)


user = 'Brad'
age = 37

print(f'The name of my mentor is {user} and he is {age} years old')